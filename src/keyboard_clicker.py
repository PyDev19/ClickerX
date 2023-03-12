# Import necessary modules.
from pynput.keyboard import Controller, Key
import time
import threading

# Define AutoClicker class and make is inherit Thread class.
class KeyboardClicker(threading.Thread):
    '''
    A class for creating an KeyboardClicker that inherits from the Thread class.
    '''
    # Initialize class variables.
    def __init__(self, keyboard: Controller, delay: float, key: Key):
        '''
        Initialize a new KeyboardClicker object.
        
        Args:
            keyboard (Controller): The mouse controller object used to simulate mouse clicks.
            delay (float): The delay between each mouse click in seconds.
            button (key): The button to be autoclicked (Left, Right, Middle).
        '''
        super(KeyboardClicker, self).__init__()
        self.keyboard = keyboard
        self.delay = delay
        self.key = key
        self.running = False
        self.program_running = True

    # Define function to start autoclicker.
    def start_clicking(self):
        self.running = True

    # Define function to stop autoclicker.
    def stop_clicking(self):
        self.running = False

    # Define function to exit autoclicker.
    def exit(self):
        self.stop_clicking()
        self.program_running = False

    # Define function to run the autoclicker.
    def run(self):
        while self.program_running: # Check if program is running.
            while self.running: # Check if autoclicker is running.
                self.keyboard.press(self.key) # Presses the key that is set for autoclicking.
                self.keyboard.release(self.key) # Releases the key that is set for autoclicking.
                time.sleep(self.delay) # Delays the autoclicker by the set ammount.
            time.sleep(0.1) # Delays main loop so the program doesn't crash.
