import json

config_file = 'config.json'

with open(config_file) as cf_file:
    config_dict = json.load(cf_file)


elemental_ip = config_dict['elemental_ip']
elemental_user = config_dict['elemental_user']