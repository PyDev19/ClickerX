# import necessary modules
from pynput.mouse import Controller, Button
import time
import threading

# define AutoClicker class and make is inherit Thread class
class AutoClicker(threading.Thread):
    # define init function to create all class (self) variables
    def __init__(self, mouse: Controller, delay: float, button: Button):
        super(AutoClicker, self).__init__()
        self.mouse = mouse
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    # define function to start autoclicker
    def start_clicking(self):
        self.running = True

    # define function to stop autoclicker
    def stop_clicking(self):
        self.running = False

    # define function to exit autoclicker
    def exit(self):
        self.stop_clicking()
        self.program_running = False

    # define function to run the autoclicker
    def run(self):
        while self.program_running: # checks if program is running
            while self.running: # checks if autoclicker is running
                self.mouse.click(self.button) # clicks the mouse button that is set for autoclicking
                time.sleep(self.delay) # delays the autoclicker by set ammount
            time.sleep(0.1) # delays main loop so the program doesn't crash

