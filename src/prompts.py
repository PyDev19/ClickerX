# Import the necessary modules.
from typing import Tuple
from pynput.mouse import Button
from configparser import ConfigParser
import os

# Import color module
from src.colors.constants import END_INFO_COLOR, RESET, INPUT_COLOR, USER_INPUT_COLOR, FIRST_INFO_COLOR, FINAL_INFO_COLOR

# Import key module
from src.classes.key import Key

# Import get mode module
from src.mode import get_mode

# Import config prompt module
from src.settings import config_prompt, create_cfg

loaded_setting = None
button_map = {"left mouse": Button.left, "right mouse": Button.right, "middle mouse": Button.middle}
key = Key()

# Function to get user input for toggle key, exit key, delay, and button to be autoclicked.
def prompts() -> Tuple[str, str, str, float, Button, str, str, str, str, str, str]:
    '''
    Prompts the user to input toggle_key, exit_key, delay, and button to be autoclicked.
    Returns a tuple containing toggle_key, exit_key, delay, and button values entered by the user.
    
    Args:
        None
        
    Returns:
        Tuple[str, str, str, float, Button, str, str, str, str, str, str]
    '''
    
    create_cfg()
    
    global loaded_setting
    
    config = ConfigParser()
    config.read("settings.cfg")
    
    prompt_style = config['STYLE']['prompt_style']
    input_style = config['STYLE']['input_style']
    info_style = config['STYLE']['info_style']
    process_starting_stlye = config['STYLE']['process_starting_stlye']
    process_ending_stlye = config['STYLE']['process_ending_stlye']
    end_error_style = config['STYLE']['end_error_style']
        
    if prompt_style == '' or prompt_style == 'None':
        prompt_style = INPUT_COLOR
    
    if input_style == '' or input_style == 'None':
        input_style = USER_INPUT_COLOR
    
    if info_style == '' or info_style == 'None':
        info_style = FIRST_INFO_COLOR
    
    if process_starting_stlye == '' or process_starting_stlye == 'None':
        process_starting_stlye = FIRST_INFO_COLOR
    
    if process_ending_stlye == '' or process_ending_stlye == 'None':
        process_ending_stlye = FINAL_INFO_COLOR
    
    if end_error_style == '' or end_error_style == 'None':
        end_error_style = END_INFO_COLOR
    
    # Gets mode of autoclicker by prompting the user
    mode = get_mode(f"{prompt_style}What mode of autoclick do you want to use\n1. Keyboard autoclicker (k)\n2. Mouse autoclicker (m)\n {RESET}", input_style, end_error_style, prompt_style)

    config.read("settings.cfg")
    
    if config.has_section('KEYBOARD') and mode == "k":
        if config.get('KEYBOARD', 'toggle_key') != 'None':
            toggle_key, exit_key, delay, button, loaded_setting = config_prompt(f'{prompt_style}Would you like to load from settings (y/n): {RESET}', mode, loaded_setting, input_style, process_starting_stlye, process_ending_stlye, end_error_style)
    
    elif config.has_section('MOUSE') and mode == "m":
        if config.get('MOUSE', 'toggle_key') != 'None':
            toggle_key, exit_key, delay, button, loaded_setting = config_prompt(f'{prompt_style}Would you like to load from settings (y/n): {RESET}', mode, loaded_setting, input_style, process_starting_stlye, process_ending_stlye, end_error_style)

    else:
        loaded_setting = False
    
    if not loaded_setting:
        # Get toggle key from user by calling get_key function with a prompt message.
        toggle_key = key.get_key(f"{prompt_style}Key to toggle autoclicker (press any key): {RESET}")
        # Print the toggle_key that the user has pressed.
        print(input_style + toggle_key + RESET)
        
        # Get exit key from user by calling get_key function with a prompt message.
        exit_key = key.get_key(f"{prompt_style}Key to exit program (press any key): {RESET}")
        # Print the exit_key that the user has pressed.
        print(input_style + exit_key + RESET)
        
        if mode == "k":
            # Get key to be autoclicked from user by calling get_key function with a prompt message.
            button = key.get_key(f"{prompt_style}Key to be autoclicked (press any key): {RESET}")
            # Print the button that the user has pressed.
            print(input_style + button + RESET)
            
            # Get delay between key presses in seconds from user by calling get_input function with a prompt message.
            delay = float(key.get_input(f"{prompt_style}Delay between key presses (in seconds): {input_style}"))
            print(f"{RESET}", end="")
            
        if mode == "m":
            # Get delay between key presses in seconds from user by calling get_input function with a prompt message.
            delay = float(key.get_input(f"{prompt_style}Delay between mouse clicks (in seconds): {input_style}"))
            print(f"{RESET}", end="")
            
            # Get key to be autoclicked from user by calling get_key function with a prompt message.
            button = input(f"{prompt_style}Button to be autoclicked (Left Mouse, Right Mouse, Middle Mouse): {input_style}")
            print(f"{RESET}", end="")

            # Check the button value entered by the user and assign corresponding Button enum value.
            button = button_map.get(button.lower(), None)
            if button == None:
                print(f"{end_error_style}Please enter either left mouse, right mouse, or middle mouse{RESET}")
                button = input(f"{prompt_style}Button to be autoclicked (Left Mouse, Right Mouse, Middle Mouse): {input_style}")
                print(f"{RESET}", end="")
    
    # Print information about toggle key and exit key to the console.
    print("\n")
    
    print(f"{info_style}Toggle autoclicker by pressing {toggle_key} key{RESET}")
    print(f"{info_style}Exit program by pressing {exit_key} key{RESET}")
    print(f"{info_style}Save your settings by pressing ` key{RESET}")
    print(f"{info_style}Change the style of the print messages by pressing . key{RESET}")
    
    print("\n")

    # Return the toggle key, exit key, delay, and button values to the calling function.
    return mode, toggle_key, exit_key, delay, button, prompt_style, input_style, info_style, process_starting_stlye, process_ending_stlye, end_error_style
