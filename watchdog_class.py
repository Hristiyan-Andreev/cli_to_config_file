import os
import sys
from os.path import getmtime
import threading as th
import time

class WatchDogReload():
    def __init__(self, files_to_watch, check_interval = 5, linux = True):
        '''
        @files_to_watch: Files watched for changes list of strings - e.g.\
             ['config.json','file.py']
        @check_interval: Time in seconds in between file change checks
        @linux: True if called on linux, false if called on windows
        '''
        self.files = files_to_watch
        self.start_up_edit_times = [(f, getmtime(f)) for f in self.files]
        self.check_interval = check_interval
        self.daemon = daemon

    def watch_and_reload(self):
        while True:
            time.sleep(self.check_interval)
            # Check whether a watched file has changed.
            for f, mtime in self.files:
                if getmtime(f) != mtime:
                    # One of the files has changed, so restart the script.
                    print('--> restarting')
                    # When running the script via `./daemon.py` (e.g. Linux/Mac OS), use
                    # os.execv(__file__, sys.argv)
                    # When running the script via `python daemon.py` (e.g. Windows), use
                    os.execv(sys.executable, ['python'] + sys.argv)
        