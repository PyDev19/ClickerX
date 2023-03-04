from pynput.mouse import Controller
from pynput.keyboard import Listener
from mouse_clicker import AutoClicker
from sys import exit
import prompts

toggle_key, exit_key, delay, button = prompts.prompts()

mouse = Controller()
auto_clicker = AutoClicker(mouse, delay, button)
auto_clicker.start()

def on_press(key):
    try:
        if key.char == toggle_key:
            if not auto_clicker.running:
                print("autoclicker started")
                auto_clicker.start_clicking()
            else:
                print("autoclicker stoped")
                auto_clicker.stop_clicking()
        elif key.char == exit_key:
            print("exiting program")
            auto_clicker.exit()
            exit()
    
    except AttributeError:
        if key.name == toggle_key:
            if not auto_clicker.running:
                print("autoclicker started")
                auto_clicker.start_clicking()
            else:
                print("autoclicker stoped")
                auto_clicker.stop_clicking()
        elif key.name == exit_key:
            print("exiting program")
            auto_clicker.exit()
            exit()

with Listener(on_press=on_press) as listener:
    listener.join()
