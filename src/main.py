# import necessary modules
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Listener, Controller
from sys import exit
import sys, time

# import clicker modules
from src.classes.mouse_clicker import AutoClicker
from src.classes.keyboard_clicker import KeyboardClicker

# import color modules
from src.colors.vtp import enable_vtp, disable_vtp
from src.colors.constants import RESET

# import prompts module
from src.prompts import prompts

# import settings module
from src.settings import save_settings

# import styles module
from src.styles import style_prompts

# import module to manage terminal
from src.terminal import reset_terminal

# enable vtp when program starts
enable_vtp()

# get user input through command line prompts
mode, toggle_key, exit_key, delay, button, prompt_style, input_style, info_style, process_starting_stlye, process_ending_stlye, end_error_style = prompts()

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
                    print(f"{process_starting_stlye}Autoclicker Started{RESET}")
                    auto_clicker.start_clicking()
                
                # if autoclicker is running, stop it and print a message
                else:
                    print(f"{process_ending_stlye}Autoclicker Stoped{RESET}")
                    auto_clicker.stop_clicking()
            
            # check if key pressed is the exit key
            elif key.char == exit_key:
                # disable virtual terminal processing, print a message, wait for a second , and exit the program
                print(f"{end_error_style}Exiting The Program{RESET}")
                
                disable_vtp()
                
                time.sleep(1)
                
                reset_terminal()
                auto_clicker.exit()
                exit()
            
            # check if key pressed is the backtick key
            elif key.char == '`':
                # saves the users settings based on what mode it is
                print(f"{process_starting_stlye}Saving current settings...{RESET}")
                save_settings(mode, toggle_key, exit_key, delay, button, process_ending_stlye)
            
            elif key.char == '.':
                sys.stdout.write("\033c")
                sys.stdout.flush()
                print(f"{process_starting_stlye}Entering style changing mode...{RESET}")
                style_prompts(toggle_key, exit_key)

        except AttributeError:
            # check if the pressed key is the toggle key (non character key)
            if key.name == toggle_key:
                
                # if autoclicker is not running, start it and print a message
                if not auto_clicker.running:
                    print(f"{process_starting_stlye}Autoclicker Started{RESET}")
                    auto_clicker.start_clicking()
                
                # if autoclicker is running, stop it and print a message
                else:
                    print(f"{process_ending_stlye}Autoclicker Stoped{RESET}")
                    auto_clicker.stop_clicking()
            
            # check if the pressed key is the exit key (non character key)
            elif key.name == exit_key:
                # disable virtual terminal processing, print a message , wait for a second, and exit program
                print(f"{end_error_style}Exiting The Program{RESET}")
                
                disable_vtp()
                
                time.sleep(1)
                
                reset_terminal()
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
                    print(f"{process_starting_stlye}Keyboard Clicker Started{RESET}")
                    keyboard_clicker.start_clicking()
                
                # if keyboard clicker is running, stop it and print a message
                else:
                    print(f"{process_ending_stlye}Keyboard Clicker Stoped{RESET}")
                    keyboard_clicker.stop_clicking()
            
            # check if key pressed is the exit key
            elif key.char == exit_key:
                # disable virtual terminal processing, print a message, wait for a second , and exit the program
                print(f"{end_error_style}Exiting The Program{RESET}")
                
                disable_vtp()
                
                time.sleep(1)
                
                reset_terminal()
                keyboard_clicker.exit()
                exit()
            
            # check if key pressed is the backtick key
            elif key.char == '`':
                # saves the users settings based on what mode it is
                print(f"{process_starting_stlye}Saving current settings...{RESET}")
                save_settings(mode, toggle_key, exit_key, delay, button, process_ending_stlye)
                
            elif key.char == '.':
                sys.stdout.write("\033c")
                sys.stdout.flush()
                print(f"{process_starting_stlye}Entering style changing mode...{RESET}")
                style_prompts(toggle_key, exit_key)
        
        except AttributeError:
            # check if the pressed key is the toggle key (non character key)
            if key.name == toggle_key:
                
                # if keyboard clicker is not running, start it and print a message
                if not keyboard_clicker.running:
                    print(f"{process_starting_stlye}Keyboard Clicker Started{RESET}")
                    keyboard_clicker.start_clicking()
                
                # if keyboard clicker is running, stop it and print a message
                else:
                    print(f"{process_ending_stlye}Keyboard Clicker Stoped{RESET}")
                    keyboard_clicker.stop_clicking()
            
            # check if the pressed key is the exit key (non character key)
            elif key.name == exit_key:
                # disable virtual terminal processing, print a message , wait for a second, and exit program
                print(f"{end_error_style}Exiting The Program{RESET}")
                
                disable_vtp()
                
                time.sleep(1)
                
                keyboard_clicker.exit()
                reset_terminal()
                exit()

    # create a listener that listens for key presses and calls the on_press function
    with Listener(on_press=on_press) as listener:
        listener.join()