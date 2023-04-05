# Import color module
from src.colors.constants import RESET

# Import key module
from src.classes.key import Key

# Define a function to get the key from the user, with a prompt string as a parameter.
def get_mode(prompt_string: str, input_style: str, end_error_style: str, prompt_style: str) -> str:
    '''
    Prompts the user for a key to select autoclicker mode.
    
    Args:
        prompt_string (str): A string representing the prompt to display to the user
        
    Returns:
        key (str): A key which the user pressed
    '''
    
    key = Key()
    
    mode_key = key.get_key(prompt_string)
    
    # Checks if key pressed is "k"
    if mode_key == "k":
        print(f"{input_style}AutoClicker Mode: Keyboard Clicker\n{RESET}")
        
    # Checks if key pressed is "m"
    elif mode_key == "m":
        print(f"{input_style}AutoClicker Mode: Mouse Clicker\n{RESET}")
    
    # Checks if key pressed is neither "m" or "k"
    elif mode_key != "m" or key != "k":
        print(f"{end_error_style}Please enter either 'k' or 'm'{RESET}")
        return get_mode(f"{prompt_style}What mode of autoclick do you want to use\n1. Keyboard autoclicker (k)\n2. Mouse autoclicker (m)\n {RESET}", input_style, end_error_style, prompt_style)
    
    # Return the key value to the calling function.
    return mode_key