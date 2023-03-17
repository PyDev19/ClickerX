# import necessary modules
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Listener, Controller
from sys import exit
import time

# import clicker modules
from src.classes.mouse_clicker import AutoClicker
from src.classes.keyboard_clicker import KeyboardClicker

# import color modules
from src.colors.vtp import enable_vtp, disable_vtp
from src.colors.constants import RESET, FINAL_INFO_COLOR, FIRST_INFO_COLOR, END_INFO_COLOR

# import prompts module
from src.prompts import prompts

# import settings module
from src.settings import save_settings

# import styles module
from src.styles import style_prompts

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
                    print(f"{FIRST_INFO_COLOR}autoclicker started{RESET}")
                    auto_clicker.start_clicking()
                
                # if autoclicker is running, stop it and print a message
                else:
                    print(f"{FINAL_INFO_COLOR}autoclicker stoped{RESET}")
                    auto_clicker.stop_clicking()
            
            # check if key pressed is the exit key
            elif key.char == exit_key:
                # disable virtual terminal processing, print a message, wait for a second , and exit the program
                print(f"{END_INFO_COLOR}exiting the program{RESET}")
                
                disable_vtp()
                
                time.sleep(1)
                
                auto_clicker.exit()
                exit()
            
            # check if key pressed is the backtick key
            elif key.char == '`':
                # saves the users settings based on what mode it is
                print(f"{FIRST_INFO_COLOR}saving current settings...{RESET}")
                save_settings(mode, toggle_key, exit_key, delay, button)
            
            elif key.char == '.':
                print(f"{FIRST_INFO_COLOR}Entering style changing mode...{RESET}")
                style_prompts()

        except AttributeError:
            # check if the pressed key is the toggle key (non character key)
            if key.name == toggle_key:
                
                # if autoclicker is not running, start it and print a message
                if not auto_clicker.running:
                    print(f"{FIRST_INFO_COLOR}autoclicker started{RESET}")
                    auto_clicker.start_clicking()
                
                # if autoclicker is running, stop it and print a message
                else:
                    print(f"{FINAL_INFO_COLOR}autoclicker stoped{RESET}")
                    auto_clicker.stop_clicking()
            
            # check if the pressed key is the exit key (non character key)
            elif key.name == exit_key:
                # disable virtual terminal processing, print a message , wait for a second, and exit program
                print(f"{END_INFO_COLOR}exiting the program{RESET}")
                
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
                    print(f"{FIRST_INFO_COLOR}keyboard clicker started{RESET}")
                    keyboard_clicker.start_clicking()
                
                # if keyboard clicker is running, stop it and print a message
                else:
                    print(f"{FINAL_INFO_COLOR}keyboard clicker stoped{RESET}")
                    keyboard_clicker.stop_clicking()
            
            # check if key pressed is the exit key
            elif key.char == exit_key:
                # disable virtual terminal processing, print a message, wait for a second , and exit the program
                print(f"{END_INFO_COLOR}exiting the program{RESET}")
                
                disable_vtp()
                
                time.sleep(1)
                
                keyboard_clicker.exit()
                exit()
            
            # check if key pressed is the backtick key
            elif key.char == '`':
                # saves the users settings based on what mode it is
                print(f"{FIRST_INFO_COLOR}saving current settings...{RESET}")
                save_settings(mode, toggle_key, exit_key, delay, button)
                
            elif key.char == '.':
                print(f"{FIRST_INFO_COLOR}Entering style changing mode...{RESET}")
                style_prompts()
        
        except AttributeError:
            # check if the pressed key is the toggle key (non character key)
            if key.name == toggle_key:
                
                # if keyboard clicker is not running, start it and print a message
                if not keyboard_clicker.running:
                    print(f"{FIRST_INFO_COLOR}keyboard clicker started{RESET}")
                    keyboard_clicker.start_clicking()
                
                # if keyboard clicker is running, stop it and print a message
                else:
                    print(f"{FINAL_INFO_COLOR}keyboard clicker stoped{RESET}")
                    keyboard_clicker.stop_clicking()
            
            # check if the pressed key is the exit key (non character key)
            elif key.name == exit_key:
                # disable virtual terminal processing, print a message , wait for a second, and exit program
                print(f"{END_INFO_COLOR}exiting the program{RESET}")
                
                disable_vtp()
                
                time.sleep(1)
                
                keyboard_clicker.exit()
                exit()

    # create a listener that listens for key presses and calls the on_press function
    with Listener(on_press=on_press) as listener:
        listener.join()
