import json

config_file = 'config.json'

with open(config_file) as cf_file:
    config_dict = json.load(cf_file)


perkele = config_dict['perkele']
download_csv = config_dict['download_csv']
data = config_dict['data']