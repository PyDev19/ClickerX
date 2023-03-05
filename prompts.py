from pynput.mouse import Button
from get_key import get_key

def prompts():
    toggle_key = get_key("Key to toggle autoclicker: ")
    exit_key = get_key("Key to exit program: ")
    delay = float(input("Delay between mouse clicks (in seconds): "))
    button = input("Button to be autoclicked (Left Mouse, Right Mouse, Middle Mouse): ")

    if button.lower() == "left mouse":
        button = Button.left
    elif button.lower() == "right mouse":
        button = Button.right
    elif button.lower() == "middle mouse":
        button = Button.middle
        
    print("\n")
    print("Toggle autoclicker by pressing {} key".format(toggle_key))
    print("Exit program by pressing {} key".format(exit_key))
    print("\n")

    return toggle_key, exit_key, delay, button