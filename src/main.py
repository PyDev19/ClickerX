# import necessary modules
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Listener, Controller
from sys import exit
import time

# import clicker modules
from src.clickers.mouse_clicker import AutoClicker
from src.clickers.keyboard_clicker import KeyboardClicker

# other custom modules
from src.vtp import enable_vtp, disable_vtp
from src.constants import RESET, GREEN, CYAN, RED
from src.prompts import prompts

# enable vtp when program starts
enable_vtp()

# get user input through command line prompts
mode, toggle_key, exit_key, delay, button = prompts()

if mode == 'm':
    # initialize mouse and AutoClicker object
    mouse = MouseController()
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
                    print(f"{GREEN}autoclicker started{RESET}")
                    auto_clicker.start_clicking()
                # if autoclicker is running, stop it and print a message
                else:
                    print(f"{CYAN}autoclicker stoped{RESET}")
                    auto_clicker.stop_clicking()
            # check if key pressed is the exit key
            elif key.char == exit_key:
                # disable virtual terminal processing, print a message, wait for a second , and exit the program
                print(f"{RED}exiting the program{RESET}")
                
                disable_vtp()
                
                time.sleep(1)
                
                auto_clicker.exit()
                exit()
        
        except AttributeError:
            # check if the pressed key is the toggle key (non character key)
            if key.name == toggle_key:
                # if autoclicker is not running, start it and print a message
                if not auto_clicker.running:
                    print(f"{GREEN}autoclicker started{RESET}")
                    auto_clicker.start_clicking()
                # if autoclicker is running, stop it and print a message
                else:
                    print(f"{CYAN}autoclicker stoped{RESET}")
                    auto_clicker.stop_clicking()
            # check if the pressed key is the exit key (non character key)
            elif key.name == exit_key:
                # disable virtual terminal processing, print a message , wait for a second, and exit program
                print(f"{RED}exiting the program{RESET}")
                
                disable_vtp()
                
                time.sleep(1)
                
                auto_clicker.exit()
                exit()

    # create a listener that listens for key presses and calls the on_press function
    with Listener(on_press=on_press) as listener:
        listener.join()

if mode == 'k':
    # initialize keyboard and KeyBoardClicker object
    keyboard = Controller()
    keyboard_clicker = KeyboardClicker(keyboard, delay, button)
    
    # start keyboard clicker in a seperate thread
    keyboard_clicker.start()
    
    # define a function to handle key presses
    def on_press(key):
        try:
            # check if the pressed key is the toggle key
            if key.char == toggle_key:
                # if keyboard clicker is not running, start it and print a message
                if not keyboard_clicker.running:
                    print(f"{GREEN}keyboard clicker started{RESET}")
                    keyboard_clicker.start_clicking()
                # if keyboard clicker is running, stop it and print a message
                else:
                    print(f"{CYAN}keyboard clicker stoped{RESET}")
                    keyboard_clicker.stop_clicking()
            # check if key pressed is the exit key
            elif key.char == exit_key:
                # disable virtual terminal processing, print a message, wait for a second , and exit the program
                print(f"{RED}exiting the program{RESET}")
                
                disable_vtp()
                
                time.sleep(1)
                
                keyboard_clicker.exit()
                exit()
        
        except AttributeError:
            # check if the pressed key is the toggle key (non character key)
            if key.name == toggle_key:
                # if keyboard clicker is not running, start it and print a message
                if not keyboard_clicker.running:
                    print(f"{GREEN}keyboard clicker started{RESET}")
                    keyboard_clicker.start_clicking()
                # if keyboard clicker is running, stop it and print a message
                else:
                    print(f"{CYAN}keyboard clicker stoped{RESET}")
                    keyboard_clicker.stop_clicking()
            # check if the pressed key is the exit key (non character key)
            elif key.name == exit_key:
                # disable virtual terminal processing, print a message , wait for a second, and exit program
                print(f"{RED}exiting the program{RESET}")
                
                disable_vtp()
                
                time.sleep(1)
                
                keyboard_clicker.exit()
                exit()

    # create a listener that listens for key presses and calls the on_press function
    with Listener(on_press=on_press) as listener:
        listener.join()
