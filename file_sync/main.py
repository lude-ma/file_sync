import logging
import pymtp


from file_sync.src.window import Window


# TODO: find a way to access android phone from file system
# https://github.com/ganeshrvel/openmtp

# https://drautb.github.io/2015/07/27/the-perfect-exchange-mtp-with-python/


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    device = pymtp.MTP()
    device.connect()
    print("\nConnected to device: %s" % device.get_devicename())

    window = Window()
