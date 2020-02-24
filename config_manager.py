import os
import sys
import json

class ConfigManager():
    def __init__(self):
        self.DEFAULT_CONFIG = self.load_default_cfg('default_config.json')
        self.CURRENT_CONFIG = self.load_current_cfg('config.json')
        self.NEW_CONFIG = self.load_current_cfg('config.json')


    def load_default_cfg(self, default_cfg_file):
        with open(default_cfg_file) as df_cfg_file:
            default_config = json.load(df_cfg_file)
        return default_config


    def load_current_cfg(self, current_cfg_file):
        with open(current_cfg_file) as current_cfg_file:
            current_config = json.load(current_cfg_file)
        return current_config

    def preview_changes(self):
        print('Changes:')
        for key, value in self.CURRENT_CONFIG.items():
            if self.CURRENT_CONFIG[key] != self.NEW_CONFIG[key]:
                print('{}: {} --> {}'.format(key, value, self.NEW_CONFIG[key]))


cfg = ConfigManager()
cfg.NEW_CONFIG['elemental_ip'] = '192.168.2.15'
cfg.NEW_CONFIG['elemental_pass'] = 'pass'

cfg.preview_changes()
