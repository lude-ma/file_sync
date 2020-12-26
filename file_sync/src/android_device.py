import logging
import os
import pymtp


class AndroidDevice(object):
    """
    https://drautb.github.io/2015/07/27/the-perfect-exchange-mtp-with-python/
    """
    def __init__(self, lst_files_synced):
        self._lst_files_synced = lst_files_synced
        self._device = pymtp.MTP()

        self._lst_files_to_sync = list()

    def connect(self):
        """Establish a connection to the android device (via USB).

        :return: Nothing
        """
        self._device.connect()
        logging.info('Connected to %s' % self._device.get_devicename())

    def disconnect(self):
        """Disconnect the android device.

        :return: Nothing
        """
        self._device.disconnect()

    def _get_dcim_folder_id(self):
        """Get folder ids for DCIM (camera folders) on internal and external
        storage.

        :return: List of (unique) folder ids.
        """
        dcim_ids = list()
        for folder in self._device.get_parent_folders():
            if folder.name == "DCIM":
                if folder.folder_id not in dcim_ids:
                    dcim_ids.append(folder.folder_id)
        logging.info('Found {} DCIM folders.'.format(len(dcim_ids)))
        return dcim_ids

    def _get_child_folders(self, parent_folder_id):
        """Get folder ids of child folders inside DCIM folders on internal and
        external storage.

        :param parent_folder_id: List of DCIM folder ids as got e.g. from
            running self.get_parent_folder_id.
        :type parent_folder_id: list
        :return: List of (unique) folder ids.
        """
        folder_ids = parent_folder_id
        all_folders = self._device.get_folder_list()

        current_length = len(folder_ids)
        new_length = None
        while current_length != new_length:
            current_length = len(folder_ids)

            for key in all_folders:
                f = all_folders[key]
                if f.parent_id in folder_ids:
                    if f.folder_id not in folder_ids:
                        folder_ids.append(f.folder_id)

            new_length = len(folder_ids)

        logging.info('Found {} child folders in DCIM '
                     'folders.'.format(len(folder_ids)))
        return folder_ids

    def _get_picture_file_list(self, folder_ids):
        """Get a filtered list of files inside given folders.

        :param folder_ids: A list of folder ids.
        :type folder_ids: list
        :return: List of files.
        """
        picture_files = []
        for f in self._device.get_filelisting():
            if f.parent_id in folder_ids:
                if (
                        f.filename.startswith('IMG_') and
                        f.filename.endswith('.jpg') or
                        f.filename.startswith('VID_') and
                        f.filename.endswith('.mp4')
                ):
                    if f.filename in self._lst_files_synced:
                        continue
                    picture_files.append(f)

        return picture_files

    def get_files_to_sync(self):
        """Get image and movie files inside all folders named 'DCIM' on both
        internal and external storage and store them in private class member
        '_lst_files_to_sync'.

        :return: Nothing
        """
        dcim_folder_id = self._get_dcim_folder_id()
        logging.debug("DCIM folder id: %s" % dcim_folder_id)

        folder_ids = self._get_child_folders(dcim_folder_id)
        logging.debug("Folder Ids: %s" % folder_ids)

        self._lst_files_to_sync = self._get_picture_file_list(folder_ids)
        for f in self._lst_files_to_sync:
            logging.debug("Picture: %s - %s" % (f.filename, f.filesize))

    def sync(self, target, remove_synced=False):
        """Sync all new image and movie files not already in target.

        :param target: The target directory.
        :type target: Directory
        :param remove_synced: Flag whether to remove the synced files from the
            android device.
        :type remove_synced: Boolean
        :return: A list containing the names of the synced files.
        """
        synced_names = list()
        files_to_sync = list()
        for f in self._lst_files_to_sync:
            if f.filename not in target:
                files_to_sync.append(f)
        nr_new = len(files_to_sync)
        for idx, f in enumerate(files_to_sync):
            logging.info('Syncing {} of {}'.format(idx, nr_new))
            tn = os.path.join(target.path, f.filename)
            self._device.get_file_to_file(file_id=f, target=tn)
            if remove_synced:
                self._device.delete_object(f)
            synced_names.append(f.filename)
        return synced_names
