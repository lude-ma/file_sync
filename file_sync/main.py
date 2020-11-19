import logging


from file_sync.src.window import Window


# TODO: find a way to access android phone from file system
# https://github.com/ganeshrvel/openmtp
# https://github.com/JeffLIrion/adb_shell
# https://github.com/google/python-adb


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    window = Window()
