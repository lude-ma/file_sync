import logging


from file_sync.src.sync_new import sync


TARGET_LOCATION = '/Users/marvin/Desktop/test_file_sync'
REMOVE_SYNCED = False


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    sync(TARGET_LOCATION, remove_synced=REMOVE_SYNCED)
