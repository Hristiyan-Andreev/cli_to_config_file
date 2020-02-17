import click as cl
import PyInquirer as pyq
import sys


# Dict of main menu options - to avoid using strings in the whole program
mm_options = {
    'stream_option': 'Stream-GPI pairs\n',
    'avail_option': 'Minimum avail duration\n'

}

av_options = {
    'enable_option': 'Enable minimum avail duration\n',
    'duration_option': 'Set duration\n'
}

def avail_menu():
    avail_options_promt = {
        'type': 'list',
        'name': 'avail_option',
        'message': 'Avail duration options',
        'choices': [av_options['enable_option'], av_options['duration_option']]
    }

    avail_options = pyq.prompt(avail_options_promt)

    if avail_options['avail_option'] is av_options['enable_option']:

        enable_options_promt = {
        'type': 'list',
        'name': 'enable_option',
        'message': 'Do you want to enable minimum avail duration',
        'choices': ['Yes', 'No']
        }

        enable_options = pyq.prompt(enable_options_promt)

        #TODO: Call a function to write in the config file
        if enable_options['enable_option'] is 'Yes':
            print('Minimum avail duration Enabled')
        elif enable_options['enable_option'] is 'No':
            print('Minimum avail duration Disabled')

    elif avail_options['avail_option'] is av_options['duration_option']:
        duration_option_promt = {
            'type': 'input',
            'name': 'avail_duration',
            'message': 'Enter the minimum avail duration in seconds',
            # 'default': 3,
            'filter': lambda val: float(val)
        }

        duration_option = pyq.prompt(duration_option_promt)
        print(duration_option['avail_duration'])
        

def main_menu():
    main_options_promt = {
        'type': 'list',
        'name': 'main_option',
        'message': 'What you want to configure?',
        'choices': [ mm_options['stream_option'], mm_options['avail_option']]
    }

    answers = pyq.prompt(main_options_promt)
    return answers
    
def whole_menu():

    while(True):
        mm_answers = main_menu()

        if mm_answers['main_option'] is mm_options['stream_option']:
            print('Perkele!')
        elif mm_answers['main_option'] is mm_options['avail_option']:
            avail_menu()


if __name__ == '__main__':
    try:
        whole_menu()
    except KeyboardInterrupt:
        print('Bye bye')