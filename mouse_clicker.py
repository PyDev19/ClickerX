# Import necessary modules.
from pynput.mouse import Controller, Button
import time
import threading

# Define AutoClicker class and make is inherit Thread class.
class AutoClicker(threading.Thread):
    '''
    A class for creating an autoclicker that inherits from the Thread class.
    '''
    # Initialize class variables.
    def __init__(self, mouse: Controller, delay: float, button: Button):
        '''
        Initialize a new AutoClicker object.
        
        Args:
            mouse (Controller): The mouse controller object used to simulate mouse clicks.
            delay (float): The delay between each mouse click in seconds.
            button (Button): The button to be autoclicked (Left, Right, Middle).
        '''
        super(AutoClicker, self).__init__()
        self.mouse = mouse
        self.delay = delay
        self.button = button
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
                self.mouse.click(self.button) # Click the mouse button that is set for autoclicking.
                time.sleep(self.delay) # Delays the autoclicker by the set ammount.
            time.sleep(0.1) # Delays main loop so the program doesn't crash.

