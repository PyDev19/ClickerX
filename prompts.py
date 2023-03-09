# Import the necessary modules.
from typing import Tuple
from pynput.mouse import Button
from get_key import get_key
import msvcrt

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
def prompts() -> Tuple[str, str, float, Button]:
    '''
    Prompts the user to input toggle_key, exit_key, delay, and button to be autoclicked.
    Returns a tuple containing toggle_key, exit_key, delay, and button values entered by the user.
    
    Args:
        None
        
    Returns:
        A tuple containing toggle_key (str), exit_key (str), delay (float), and button (Button enum value).
    '''
    
    # Get toggle key from user by calling get_key function with a prompt message.
    # \033[34m is for giving blue color to print message and \033[0m is to reset the color back to normal
    toggle_key = get_key("\033[34mKey to toggle autoclicker (press any key): \033[0m")
    
    # Get exit key from user by calling get_key function with a prompt message.
    # \033[34m is for giving blue color to print message and \033[0m is to reset the color back to normal
    exit_key = get_key("\033[34mKey to exit program (press any key): \033[0m")
    
    # Get delay between mouse clicks in seconds from user by calling get_input function with a prompt message.
    # \033[34m is for giving blue color to print message and \033[33m is for giving yellow color to the user input
    delay = float(get_input("\033[34mDelay between mouse clicks (in seconds): \033[33m"))
    print("\033[0m", end="") # \033[0m to reset the color back to normal
    
    # Get button to be autoclicked from user by calling input function with a prompt message.
    # \033[34m is for giving blue color to print message and \033[33m is for giving yellow color to the user input
    button = input("\033[34mButton to be autoclicked (Left Mouse, Right Mouse, Middle Mouse): \033[33m")
    print("\033[0m", end="") # \033[0m to reset the color back to normal

    # Check the button value entered by the user and assign corresponding Button enum value.
    if button.lower() == "left mouse":
        button = Button.left
    elif button.lower() == "right mouse":
        button = Button.right
    elif button.lower() == "middle mouse":
        button = Button.middle
        
    # Print information about toggle key and exit key to the console.
    # \033[36m is to add cyan color to the print meesage and \033[0m is to reset the color back to norma
    print("\n")
    print(f"\033[36mToggle autoclicker by pressing {toggle_key} key\033[0m")
    print(f"\033[36mExit program by pressing {exit_key} key\033[0m")
    print("\n")

    # Return the toggle key, exit key, delay, and button values to the calling function.
    return toggle_key, exit_key, delay, button
