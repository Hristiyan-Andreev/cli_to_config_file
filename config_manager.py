import os
import sys
import json

class ConfigManager():
    def __init__(self):
        self.DEFAULT_CONFIG = {}
        self.CURRENT_CONFIG = {}
        self.NEW_CONFIG = {}
       
        self.load_default_cfg('default_config.json')

        current_config = 'config.json'
        with open(current_config) as current_cfg:
            self.CURRENT_CONFIG = json.load(current_cfg)

        self.NEW_CONFIG = self.CURRENT_CONFIG

    def load_default_cfg(self, default_config):
        with open(default_config) as df_config_file:
            self.DEFAULT_CONFIG = json.load(df_config_file)