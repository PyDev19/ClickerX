# Import the necessary modules.
from pynput.mouse import Button
from get_key import get_key
import msvcrt

# Defines function to get user input with a prompt string and returns user input string.
def get_input(prompt: str) -> str:
    # Loop to check if a key press is waiting to be processed.
    while msvcrt.kbhit():
        # Function to block a pending key press.
        msvcrt.getch()
    
    # Get input from user by asking prompt string from function parameter.
    user_input = input(prompt)
    
    # Return the user input value to the calling function.
    return user_input


# Function to get user input for toggle key, exit key, delay, and button to be autoclicked.
def prompts():
    # Get toggle key from user by calling get_key function with a prompt message.
    toggle_key = get_key("Key to toggle autoclicker (press any key): ")
    
    # Get exit key from user by calling get_key function with a prompt message.
    exit_key = get_key("Key to exit program (press any key): ")
    
    # Get delay between mouse clicks in seconds from user by calling get_input function with a prompt message.
    delay = float(get_input("Delay between mouse clicks (in seconds): "))
    
    # Get button to be autoclicked from user by calling input function with a prompt message.
    button = input("Button to be autoclicked (Left Mouse, Right Mouse, Middle Mouse): ")

    # Check the button value entered by the user and assign corresponding Button enum value.
    if button.lower() == "left mouse":
        button = Button.left
    elif button.lower() == "right mouse":
        button = Button.right
    elif button.lower() == "middle mouse":
        button = Button.middle
        
    # Print information about toggle key and exit key to the console.
    print("\n")
    print("Toggle autoclicker by pressing {} key".format(toggle_key))
    print("Exit program by pressing {} key".format(exit_key))
    print("\n")

    # Return the toggle key, exit key, delay, and button values to the calling function.
    return toggle_key, exit_key, delay, button
