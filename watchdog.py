# !/usr/bin/env python3

import os
import sys
from os.path import getmtime

import config as cf

# Parse script arguments and configuration files.
# ...

WATCHED_FILES = ['config.py']
WATCHED_FILES_MTIMES = [(f, getmtime(f)) for f in WATCHED_FILES]
print(cf.perkele)

while True:
    # Wait for inputs and act on them.

    # Check whether a watched file has changed.
    for f, mtime in WATCHED_FILES_MTIMES:
        if getmtime(f) != mtime:
            # One of the files has changed, so restart the script.
            print('--> restarting')
            # When running the script via `./daemon.py` (e.g. Linux/Mac OS), use
            # os.execv(__file__, sys.argv)
            # When running the script via `python daemon.py` (e.g. Windows), use
            os.execv(sys.executable, ['python'] + sys.argv)

