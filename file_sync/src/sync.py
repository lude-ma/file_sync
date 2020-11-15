import logging
import os
import shutil


from bookkeeping import BookKeeper
from directory import Directory


def sync(fp_source, fp_target, create_copy):
    bk = BookKeeper()
    lst_synced = bk.read()
    lst_source = Directory(fp_source)
    lst_target = Directory(fp_target)

    count = 0
    what = 'copied' if create_copy else 'moved'

    for source in lst_source:
        if source not in lst_synced and source not in lst_target:
            full_source = os.path.join(lst_source.path, source)
            full_target = os.path.join(lst_target.path, source)
            if create_copy:
                shutil.copy(full_source, full_target)
            else:
                shutil.move(full_source, full_target)
            bk.write(source)
            count += 1
            logging.debug('{}: {} {}'.format(lst_source.path,
                                             what,
                                             source))
        else:
            if source in lst_synced:
                logging.debug('{}: {} already synced'.format(lst_source.path,
                                                             source))

            if source in lst_target:
                logging.debug('{}: {} at target location'.format(lst_source.path,
                                                                 source))
    logging.info('{} {} of {} files from {} to {}.'.format(what, count,
                                                           len(lst_source),
                                                           lst_source.path,
                                                           lst_target.path))
