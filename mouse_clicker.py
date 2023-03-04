import time
import threading

class AutoClicker(threading.Thread):
    def __init__(self, mouse, delay, button):
        super(AutoClicker, self).__init__()
        self.mouse = mouse
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                self.mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)

