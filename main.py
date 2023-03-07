# import necessary modules
from pynput.mouse import Controller
from pynput.keyboard import Listener
from mouse_clicker import AutoClicker
from sys import exit
import prompts, time

# get user input through command line prompts
toggle_key, exit_key, delay, button = prompts.prompts()

# initialize mouse and AutoClicker object
mouse = Controller()
auto_clicker = AutoClicker(mouse, delay, button)

# start autoclicker in a seperate thread
auto_clicker.start()

# define a function to handle key presses
def on_press(key):
    try:
        # check if the pressed key is the toggle key
        if key.char == toggle_key:
            # if autoclicker is not running, start it and print a message
            if not auto_clicker.running:
                print("autoclicker started")
                auto_clicker.start_clicking()
            # if autoclicker is running, stop it and print a message
            else:
                print("autoclicker stoped")
                auto_clicker.stop_clicking()
        # check if key pressed is the exit key
        elif key.char == exit_key:
            # print a message, wait for a second exit the program
            print("exiting program")
            auto_clicker.exit()
            exit()
    
    except AttributeError:
        # check if the pressed key is the toggle key (non character key)
        if key.name == toggle_key:
            # if autoclicker is not running, start it and print a message
            if not auto_clicker.running:
                print("autoclicker started")
                auto_clicker.start_clicking()
            # if autoclicker is running, stop it and print a message
            else:
                print("autoclicker stoped")
                auto_clicker.stop_clicking()
        # check if the pressed key is the exit key (non character key)
        elif key.name == exit_key:
            # print a message , wait for a second, and exit program
            print("exiting program")
            time.sleep(1)
            auto_clicker.exit()
            exit()

# create a listener that listens for key presses and calls the on_press function
with Listener(on_press=on_press) as listener:
    listener.join()
