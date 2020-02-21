# !/usr/bin/env python3

import os
import sys
from os.path import getmtime
import threading as th
import time

import config as cf

WATCHED_FILES = ['config.json']
WATCHED_FILES_MTIMES = [(f, getmtime(f)) for f in WATCHED_FILES]
print('\n{}'.format(cf.perkele))


def watch_reload_func():

    while True:
        time.sleep(5)
        # Check whether a watched file has changed.
        for f, mtime in WATCHED_FILES_MTIMES:
            if getmtime(f) != mtime:
                # One of the files has changed, so restart the script.
                print('--> restarting')
                # When running the script via `./daemon.py` (e.g. Linux/Mac OS), use
                # os.execv(__file__, sys.argv)
                # When running the script via `python daemon.py` (e.g. Windows), use
                os.execv(sys.executable, ['python'] + sys.argv)

reload_thread = th.Thread(target=watch_reload_func)
reload_thread.start()

import watchdog_class as wtd

wtd.WatchDogReload()