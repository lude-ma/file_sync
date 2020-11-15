import os

location = __file__
location = os.path.split(location)[0]
location = os.path.split(location)[0]

location = os.path.join(location, 'logs')
FN_BOOKKEEPING = os.path.join(location, 'bookkeeping.txt')

WINDOW_NAME = 'file sync v0.1'
