"""Utils module"""

import os


def clear_screen():
    """Function clearing console screen"""

    os.system('clear')

def press_key():
    """Function waiting user to press any key"""

    try:
        input('Press any key to continue...')
    except KeyboardInterrupt:
        pass
    clear_screen()

def is_list_items_equals(list_, value):
    """Cheking if any element in list is equals to the value"""
    return len(list(filter(lambda x: x == value, list_))) == len(list_)
