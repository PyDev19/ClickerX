# Import the necessary modules.
from typing import Tuple
from pynput.mouse import Button
from configparser import ConfigParser
import msvcrt, os

# Import colors modules
from src.keys.get_key import get_key
from src.keys.get_mode import get_mode
from src.settings import config_prompt
from src.colors.constants import RED, RESET, BLUE, YELLOW, CYAN

loaded_setting = None
button_map = {"left mouse": Button.left, "right mouse": Button.right, "middle mouse": Button.middle}

# Defines function to get user input with a prompt string and returns user input string.
def get_input(prompt: str) -> str:
    """
    Clears any key presses waiting to be processed and gets user input from the console and returns it as a string.

    Args:
        prompt: A string representing the prompt to display to the user.

    Returns:
        A string representing the user's input.
    """
    
    # Loop to check if a key press is waiting to be processed.
    while msvcrt.kbhit():
        # Function to block a pending key press.
        msvcrt.getch()
    
    # Get input from user by asking prompt string from function parameter.
    user_input = input(prompt)
    
    # Return the user input value to the calling function.
    return user_input

# Function to get user input for toggle key, exit key, delay, and button to be autoclicked.
def prompts() -> Tuple[str, str, str, float, Button]:
    '''
    Prompts the user to input toggle_key, exit_key, delay, and button to be autoclicked.
    Returns a tuple containing toggle_key, exit_key, delay, and button values entered by the user.
    
    Args:
        None
        
    Returns:
        A tuple containing mode (str, toggle_key (str), exit_key (str), delay (float), and button (Button enum value).
    '''
    
    global loaded_setting
    
    config = ConfigParser()
    
    # Gets mode of autoclicker by prompting the user
    mode = get_mode(f"{BLUE}What mode of autoclick do you want to use\n1. Keyboard autoclicker (k)\n2. Mouse autoclicker (m)\n {RESET}")
    
    if os.path.exists('settings.cfg'):
        config.read("settings.cfg")
        
        if config.has_section('KEYBOARD') and mode == "k":
            toggle_key, exit_key, delay, button, loaded_setting = config_prompt(f'{BLUE}Would you like to load from settings (y/n): {RESET}', mode, loaded_setting)
        
        elif config.has_section('MOUSE') and mode == "m":
            toggle_key, exit_key, delay, button, loaded_setting = config_prompt(f'{BLUE}Would you like to load from settings (y/n): {RESET}', mode, loaded_setting)

        else:
            loaded_setting = False
    
    if not loaded_setting:
        # Get toggle key from user by calling get_key function with a prompt message.
        toggle_key = get_key(f"{BLUE}Key to toggle autoclicker (press any key): {RESET}")
        
        # Get exit key from user by calling get_key function with a prompt message.
        exit_key = get_key(f"{BLUE}Key to exit program (press any key): {RESET}")
        
        if mode == "k":
            # Get key to be autoclicked from user by calling get_key function with a prompt message.
            button = get_key(f"{BLUE}Key to be autoclicked (press any key): {RESET}")
            
            # Get delay between key presses in seconds from user by calling get_input function with a prompt message.
            delay = float(get_input(f"{BLUE}Delay between key presses (in seconds): {YELLOW}"))
            print(f"{RESET}", end="")
            
        if mode == "m":
            # Get delay between key presses in seconds from user by calling get_input function with a prompt message.
            delay = float(get_input(f"{BLUE}Delay between mouse clicks (in seconds): {YELLOW}"))
            print(f"{RESET}", end="")
            
            # Get key to be autoclicked from user by calling get_key function with a prompt message.
            button = input(f"{BLUE}Button to be autoclicked (Left Mouse, Right Mouse, Middle Mouse): {YELLOW}")
            print(f"{RESET}", end="")

            # Check the button value entered by the user and assign corresponding Button enum value.
            button = button_map.get(button.lower(), None)
            if button == None:
                print(f"{RED}Please enter either left mouse, right mouse, or middle mouse{RESET}")
                button = input(f"{BLUE}Button to be autoclicked (Left Mouse, Right Mouse, Middle Mouse): {YELLOW}")
                print(f"{RESET}", end="")
        
    # Print information about toggle key and exit key to the console.
    print("\n")
    
    print(f"{CYAN}Toggle autoclicker by pressing {toggle_key} key{RESET}")
    print(f"{CYAN}Exit program by pressing {exit_key} key{RESET}")
    print(f"{CYAN}Save your settings by pressing ` key{RESET}")
    
    print("\n")

    # Return the toggle key, exit key, delay, and button values to the calling function.
    return mode, toggle_key, exit_key, delay, button
