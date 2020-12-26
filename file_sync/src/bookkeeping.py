import os


from file_sync import FN_BOOKKEEPING


class BookKeeper(object):
    def __init__(self):
        basedir = os.path.dirname(FN_BOOKKEEPING)
        if not os.path.exists(basedir):
            os.makedirs(basedir)
        self._file = FN_BOOKKEEPING

    def read(self):
        lst_files = list()
        try:
            with open(self._file, 'r') as fp:
                for row in fp:
                    if row.endswith('\n'):
                        lst_files.append(row[:-1])
                    else:
                        lst_files.append(row)
        except Exception:
            pass
        return lst_files

    def write(self, data):
        with open(self._file, 'a') as fp:
            if isinstance(data, list):
                for d in data:
                    fp.write('{}\n'.format(d))
            elif isinstance(data, str):
                fp.write('{}\n'.format(data))
