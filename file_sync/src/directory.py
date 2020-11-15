import os


class Directory(object):
    def __init__(self, path):
        self.path = path
        self._raw = os.listdir(self.path)
        self._data = self._filter_jpeg()

    def __iter__(self):
        return iter(self._data)

    def __next__(self):
        for d in self._data:
            return d

    def __len__(self):
        return len(self._data)

    def _filter_jpeg(self):
        lst_images = list()
        for r in self._raw:
            _, ext = os.path.splitext(r)
            if ext.lower() in ['.jpg', '.jpeg']:
                lst_images.append(r)
        return lst_images

    def show_filtered_objects(self):
        lst_filtered = list()
        for r in self._raw:
            if r not in self._data:
                lst_filtered.append(r)
        print('{}: filtered {}'.format(self.path, lst_filtered))
