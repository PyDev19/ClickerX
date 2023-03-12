# Import the necessary modules.
from pynput import keyboard
from queue import Queue
from src.colors.constants import RESET, YELLOW

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
def get_key(prompt_string: str) -> str:
    '''
    Prompts the user for a key.
    
    Args:
        prompt_string (str): A string representing the prompt to display to the user
        
    Returns:
        key (str): A key which the user pressed
    
    Raises:
        ValueError: If the user presses an invalid key.

    Examples:
        To prompt the user for a key and print the key that was pressed, use:

        >>> key = get_key("Press a key: ")
        >>> print("You pressed:", key)
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
        
        # Print the key that the user has pressed.
        print(YELLOW + key + RESET)
        
        # Return the key value to the calling function.
        return key
