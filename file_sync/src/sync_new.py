from android_device import AndroidDevice
from bookkeeping import BookKeeper
from directory import Directory


def sync(fp_target, remove_synced=False):
    bk = BookKeeper()
    lst_synced = bk.read()

    target = Directory(fp_target)

    ad = AndroidDevice(lst_synced)
    ad.connect()
    ad.get_files_to_sync()
    lst_new = ad.sync(target=target, remove_synced=remove_synced)
    ad.disconnect()
    bk.write(lst_new)
