# Import the necessary modules.
from pynput import keyboard
from queue import Queue

# Import color module
from src.colors.constants import RESET, YELLOW, RED, BLUE

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
def get_mode(prompt_string: str) -> str:
    '''
    Prompts the user for a key to select autoclicker mode.
    
    Args:
        prompt_string (str): A string representing the prompt to display to the user
        
    Returns:
        key (str): A key which the user pressed
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
        if key == "k":
            print(f"{YELLOW}AutoClicker Mode: Keyboard Clicker{RESET}")
            
        # Checks if key pressed is "m"
        elif key == "m":
            print(f"{YELLOW}AutoClicker Mode: Mouse Clicker{RESET}")
        
        # Checks if key pressed is neither "m" or "k"
        elif key != "m" or key != "k":
            print(f"{RED}Please enter either 'k' or 'm'{RESET}")
            get_mode(f"{BLUE}What mode of autoclick do you want to use\n1. Keyboard autoclicker (k)\n2. Mouse autoclicker (m)\n {RESET}")
        
        # Return the key value to the calling function.
        return key
