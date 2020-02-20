import click as cl
import PyInquirer as pyq
import sys

import validators as val


# Dict of main menu options - to avoid using strings in the whole program
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
    if elemental_answers['elemental'] is el_choices['back']:
        return True
    else:
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
        return True
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
    return answers
    
def whole_menu():

    while(True):
        mm_answers = main_menu()

        if mm_answers['main_option'] is mm_choices['elemental']:
            while(True):
                if elemental_menu(): break
                

        if mm_answers['main_option'] is mm_choices['stream']:
            print('Perkele!')

        elif mm_answers['main_option'] is mm_choices['avail']:
            while(True):
                if avail_menu(): break
                


if __name__ == '__main__':
    try:
        whole_menu()
    except KeyboardInterrupt:
        print('Bye bye')