import click as cl
import PyInquirer as pyq
import sys
import json

import validators as val
from config_manager import ConfigManager

EXIT_FLAG = 123

# # Load default config file
# default_config = 'default_config.json'
# with open(default_config) as df_config_file:
#     DEFAULT_CONFIG = json.load(df_config_file)

# print(DEFAULT_CONFIG)

# # Load current config file
# current_config = 'config.json'
# with open(current_config) as current_cfg:
#     CURRENT_CONFIG = json.load(current_cfg)

# print(CURRENT_CONFIG)

# # Dictionary to save config parameters before dumping to JSON
# NEW_CONFIG = CURRENT_CONFIG

cfg = ConfigManager()
cfg.preview_changes()


# Dicts of menu options - to avoid using strings in the whole program
mm_choices = {
    'elemental':'Elemental server - IP and credentials',
    'stream': 'Stream-GPI pairs - number of streams and GPI mapping',
    'avail': 'Minimum avail duration - Enable/Disable, Duration',
    'back': 'Exit'

}

av_choices = {
    'enable': 'Enable minimum avail duration',
    'duration': 'Set duration',
    'back': 'Go back'
}

el_choices = {
    'ip': 'Enter Elemental Live server IP address',
    'credentials': 'Enter the username and password for access',
    'back': 'Go back'
}


def elemental_menu():
    elemental_promt = [
        {
            'type': 'list',
            'name': 'elemental',
            'message': 'Elemenal Live server options\n',
            'choices': [el_choices['ip'], el_choices['credentials'], \
                        el_choices['back']]
        },
        {
            'type': 'input',
            'name': 'elemental_ip',
            'message': 'Enter the Elemenal Live server IP address - without port',
            'validate': val.IpValidator,
            'when': lambda elemental_answers: elemental_answers['elemental'] \
                 is el_choices['ip'],
            # 'filter': lambda val: float(val)
        },
        {
            'type': 'input',
            'name': 'elemental_user',
            'message': 'Enter Elemental Live username',
            'when': lambda elemental_answers: elemental_answers['elemental'] \
                 is el_choices['credentials']
        },
        {
            'type': 'password',
            'name': 'elemental_pass',
            'message': 'Enter Elemental Live password',
            'when': lambda elemental_answers: elemental_answers['elemental'] \
                 is el_choices['credentials']
        }
    ]

    elemental_answers = pyq.prompt(elemental_promt)
    if elemental_answers['elemental'] is el_choices['ip']:
        NEW_CONFIG['elemental_ip'] = elemental_answers['elemental_ip']

    elif elemental_answers['elemental'] is el_choices['credentials']:
        NEW_CONFIG['elemental_user'] = elemental_answers['elemental_user']
        NEW_CONFIG['elemental_pass'] = elemental_answers['elemental_pass']

    elif elemental_answers['elemental'] is el_choices['back']:
        print(NEW_CONFIG)
        return EXIT_FLAG

    else:
        return 0


def stream_menu():
    stream_num_promt = [
        {
            'type': 'input',
            'name': 'gpi_num',
            'message': 'Enter the number of GPI-Stream pairs',
            # 'validate':
            # 'filter': lambda input: int(input)
        }
    ]
    stream_answers = pyq.prompt(stream_num_promt)
    num_of_streams = int(stream_answers['gpi_num'])

    gpi_to_stream_map = {}
    for stream in range(1, num_of_streams+1):
        gpi_promt = [
            {
                'type': 'input',
                'name': 'gpi_{}'.format(stream),
                'message': 'Enter the GPI pin for GPI-Stream pair number ({}):'.format(stream),
                # 'validate': lambda input: not isinstance(input, int) or 'Enter an int value',
                # 'filter': lambda input: int(input)
            }
        ]
        gpi_answer = pyq.prompt(gpi_promt)
        gpi_pin = gpi_answer['gpi_{}'.format(stream)]

        stream_promt = [
            {
                'type': 'input',
                'name': 'stream_{}'.format(stream),
                'message': 'Enter the Elemental event number for GPI ({}):'.format(gpi_pin),
            }
        ]
        stream_answer = pyq.prompt(stream_promt)
        event_number = stream_answer['stream_{}'.format(stream)]

        gpi_to_stream_map[gpi_pin] = event_number
    
    print(gpi_to_stream_map)

    # if stream_answers['back']: return EXIT_FLAG

    return 0


def avail_menu():
    avails_promt = [
        {
            'type': 'list',
            'name': 'avail',
            'message': 'Avail duration options',
            'choices': [av_choices['enable'], av_choices['duration'], \
                        av_choices['back']]
        },
        {
            'type': 'list',
            'name': 'enable',
            'message': 'Do you want to enable minimum avail duration',
            'choices': ['Yes', 'No'],
            'when': lambda avails: avails['avail'] is av_choices['enable']
        },
        {
            'type': 'input',
            'name': 'avail_duration',
            'message': 'Enter the minimum avail duration in seconds',
            'validate': val.AvDurValidator,
            'when': lambda avails: avails['avail'] is av_choices['duration'],
            'filter': lambda val: float(val)
        }
    ]

    avails = pyq.prompt(avails_promt)

    if avails['avail'] is av_choices['back']:
        return EXIT_FLAG
    else:
        return 0
   

def main_menu():
    main_options_promt = {
        'type': 'list',
        'name': 'main_option',
        'message': 'What you want to configure?\n',
        'choices': [mm_choices['elemental'], mm_choices['stream'], \
                    mm_choices['avail'], mm_choices['back']]
    }

    answers = pyq.prompt(main_options_promt)

    if answers['main_option'] is mm_choices['back']:
        return EXIT_FLAG
    else:
        return answers
    

def whole_menu():

    while(True):
        mm_answers = main_menu()


        if mm_answers is EXIT_FLAG:
            break

        elif mm_answers['main_option'] is mm_choices['elemental']:
            while(True):
                if elemental_menu() is EXIT_FLAG: break                

        elif mm_answers['main_option'] is mm_choices['stream']:
            while(True):
                if stream_menu() is EXIT_FLAG: break

        elif mm_answers['main_option'] is mm_choices['avail']:
            while(True):
                if avail_menu() is EXIT_FLAG: break

    return 0


if __name__ == '__main__':
    try:
        whole_menu()
    except KeyboardInterrupt:
        print('Will miss you')
    finally:
        print('We are done!')