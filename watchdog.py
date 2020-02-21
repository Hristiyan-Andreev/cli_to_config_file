# !/usr/bin/env python3

import os
# import sys
# from os.path import getmtime
# import threading as th
import time
import watchdog_class as wtd

import config as cf


def main():
    WATCHED_FILES = ['config.json']

    reload_thread = wtd.WatchDogReload(WATCHED_FILES, linux=False)
    reload_thread.start()

    while(True):
        print(cf.config_dict)
        time.sleep(5)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Bye bye')

