# Import the necessary modules.
import os
from pynput import keyboard
from queue import Queue
from configparser import ConfigParser

# Import color module
from src.colors.constants import CYAN, GREEN, RESET, YELLOW, RED, BLUE

# Define the function that will be called when a key is pressed.
def on_press(key: keyboard.Key) -> None:
    pass

# Define the function that will be called when a key is released.
def on_release(key: keyboard.Key, queue: Queue) -> None:
    try:
        # Put the character key in the queue.
        queue.put(key.char)
    
    except AttributeError:
        # Put non-character keys in the queue.
        queue.put(key.name)

# Define a function to get the key from the user, with a prompt string as a parameter.
def config_prompt(prompt_string: str, mode: str):
    '''
    Prompts the user for a key to load config.
    
    Args:
        prompt_string (str): A string representing the prompt to display to the user
    '''
    
    # Create a new queue object to hold the key value.
    key_queue = Queue()
    
    # Start a keyboard listener with the on_press and on_release functions.
    # Use a lambda function to pass the queue object to the on_release function.
    with keyboard.Listener(on_press=on_press, on_release=lambda key: on_release(key, queue=key_queue)):
        # Print the prompt string to the console.
        # Use flush=True to ensure that the message is printed immediately.
        # Use end='' to make sure that the next print statement is on the same line.
        print(prompt_string, end='', flush=True)
        
        # Initialize the key value to None.
        key = None
        
        # Keep looping until a key value has been retrieved from the queue.
        while key is None:
            key = key_queue.get()
        
        # Checks if key pressed is "k"
        if key == "y":
            print(f"{YELLOW}{key}{RESET}")
            print(f"{CYAN}Loading Conifg...{RESET}")
            toggle_key, exit_key, delay, button = read_settings(mode)
            print(f"{GREEN}Done loading from config!{RESET}")
            
        # Checks if key pressed is "m"
        elif key == "n":
            print(f"{YELLOW}Continuing to prompts...{RESET}")
        
        # Checks if key pressed is neither "m" or "k"
        elif key != "y" or key != "n":
            print(f"{RED}Please enter either 'y' or 'n'{RESET}")
            config_prompt('Would you like to load from settings (y/n): ', mode)
        
        return toggle_key, exit_key, delay, button

def save_settings(mode: str, toggle_key: str, exit_key: str, delay: float, button: str):
    config = ConfigParser()
    
    if mode == "k":
        config['KEYBOARD'] = {'toggle_key': toggle_key, 'exit_key': exit_key, 'delay': delay, 'button': button}
    elif mode == "m":
        config['MOUSE'] = {'toggle_key': toggle_key, 'exit_key': exit_key, 'delay': delay, 'button': button}
    
    with open('settings.cfg', 'w') as config_file:
        config.write(config_file)
    
    print(f"{BLUE}done saving settings, you can continue using autoclicker now{RESET}")    

def read_settings(mode):
    config = ConfigParser()
    config.read('settings.cfg')
    
    if mode == "m":
        section = "MOUSE"
    elif mode == "k":
        section == "KEYBOARD"
    
    toggle_key = config[section]['toggle_key']
    exit_key = config[section]['exit_key']
    delay = config[section]['delay']
    button = config[section]['button']
    
    return toggle_key, exit_key, delay, button
