# Import the necessary modules.
import os
from pynput.mouse import Button
from configparser import ConfigParser

# Import color module
from src.colors.constants import RESET

# Import key module
from src.classes.key import Key

button_map = {"Button.left": Button.left, "Button.right": Button.right, "Button.middle": Button.middle}
key = Key()

def create_cfg():
    if not os.path.exists('settings.cfg'):
        with open('settings.cfg', mode="x") as file:
            file.write('[KEYBOARD]\n')
            file.write('toggle_key = None\n')
            file.write('exit_key = None\n')
            file.write('delay = None\n')
            file.write('button = None\n\n')
            
            file.write('[MOUSE]\n')
            file.write('toggle_key = None\n')
            file.write('exit_key = None\n')
            file.write('delay = None\n')
            file.write('button = None\n\n')
            
            file.write('[STYLE]\n')
            file.write('prompt_style = None\n')
            file.write('input_style = None\n')
            file.write('info_style = None\n')
            file.write('process_starting_stlye = None\n')
            file.write('process_ending_stlye = None\n')
            file.write('end_error_style = None')
            
            file.close()

# Define a function to get the key from the user, with a prompt string as a parameter.
def config_prompt(
    prompt_string: str, 
    mode: str, 
    load_settings: bool, 
    input_style: str, 
    process_starting_stlye: str, 
    process_ending_stlye: str, 
    end_error_style: str
):
    '''
    Prompts the user for a key to load config.
    
    Args:
        prompt_string (str): A string representing the prompt to display to the user
    '''
    
    input_key = key.get_key(prompt_string)
    
    # Checks if key pressed is "y"
    if input_key == "y":
        print(f"{input_style}{input_key}{RESET}")
        print(f"{process_starting_stlye}Loading Conifg...{RESET}")
        
        toggle_key, exit_key, delay, button = read_settings(mode)
        load_settings = True
        
        print(f"{process_ending_stlye}Done loading from config!{RESET}")
        
    # Checks if key pressed is "n"
    elif input_key == "n":
        print(f"{input_style}{input_key}{RESET}")
        print(f"{process_ending_stlye}Continuing to prompts...{RESET}")
        
        load_settings = False
        toggle_key = None
        exit_key = None
        delay = None
        button = None
    
    # Checks if key pressed is neither "y" or "n"
    elif input_key != "y" or input_key != "n":
        print(f"{end_error_style}Please enter either 'y' or 'n'{RESET}")
        config_prompt('Would you like to load from settings (y/n): ', mode, load_settings, input_style, process_starting_stlye, process_ending_stlye, end_error_style)
    
    return toggle_key, exit_key, delay, button, load_settings

def save_settings(
    mode: str, 
    toggle_key: str, 
    exit_key: str, 
    delay: float, 
    button: str, 
    process_ending_stlye: str
):
    config = ConfigParser()
    
    config.read('settings.cfg')
    
    if mode == "k":
        if 'KEYBOARD' in config:
            config.remove_section('KEYBOARD')
            with open('settings.cfg', 'w') as config_file:
                config.write(config_file)
        
        config['KEYBOARD'] = {
            'toggle_key': toggle_key, 
            'exit_key': exit_key, 
            'Delay': delay, 
            'button': button
        }
        
        with open('settings.cfg', 'w') as config_file:
            config.write(config_file)
        
    elif mode == "m":
        if 'MOUSE' in config:
            config.remove_section('MOUSE')
            with open('settings.cfg', 'w') as config_file:
                config.write(config_file)
        
        config['MOUSE'] = {
            'toggle_key': toggle_key, 
            'exit_key': exit_key, 
            'Delay': delay, 
            'button': str(button)
        }
        
        with open('settings.cfg', 'w') as config_file:
            config.write(config_file)
    
    print(f"{process_ending_stlye}done saving settings, you can continue using autoclicker now{RESET}")

def save_styles_settings(prompt: str, input: str, info: str, starting: str, stopping: str, exit: str):
    config = ConfigParser()
    
    config.read('settings.cfg')
    
    if 'STYLE' in config:
        config.remove_section('STYLE')
        with open('settings.cfg', 'w') as config_file:
            config.write(config_file)
    
    config['STYLE'] = {
        'prompt_style': str(prompt), 
        'input_style': str(input), 
        'info_style': str(info), 
        'process_starting_stlye': str(starting),
        'process_ending_stlye': str(stopping),
        'end_error_style': str(exit)
    }
    
    with open('settings.cfg', 'w') as config_file:
        config.write(config_file)

def read_settings(mode):
    config = ConfigParser()
    config.read('settings.cfg')
    
    if mode == "m":
        section = "MOUSE"
    elif mode == "k":
        section = "KEYBOARD"
    
    toggle_key = config[section]['toggle_key']
    exit_key = config[section]['exit_key']
    delay = float(config[section]['delay'])
    
    if mode == "m":
        button = config[section]['button']
        button = button_map.get(button, None)
    elif mode == "k":
        button = config[section]['button']
    
    
    return toggle_key, exit_key, delay, button
