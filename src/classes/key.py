# Import the necessary modules.
import msvcrt
from pynput.keyboard import Key as KeyType, Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
from queue import Queue

class Key:
    def __init__(self) -> None:
        pass
    
    # Define the function that will be called when a key is pressed.
    def on_press(self, key: KeyType) -> None:
        pass
    
    # Define the function that will be called when a key is released.
    def on_release(self, key: KeyType, queue: Queue) -> None:
        try:
            # Put the character key in the queue.
            queue.put(key.char)
        
        except AttributeError:
            # Put non-character keys in the queue.
            queue.put(key.name)
    
    def get_key(self, prompt_string: str) -> str:
        '''
        Prompts the user for a key.
        
        Args:
            prompt_string (str): A string representing the prompt to display to the user
            
        Returns:
            key (str): A key which the user pressed

        Examples:
            To prompt the user for a key and print the key that was pressed, use:

            >>> key = get_key("Press a key: ")
            >>> print("You pressed:", key)
        '''
        
        # Create a new queue object to hold the key value.
        key_queue = Queue()
        
        # Start a keyboard listener with the on_press and on_release functions.
        # Use a lambda function to pass the queue object to the on_release function.
        with KeyboardListener(on_press=self.on_press, on_release=lambda key: self.on_release(key, queue=key_queue)):
            # Print the prompt string to the console.
            # Use flush=True to ensure that the message is printed immediately.
            # Use end='' to make sure that the next print statement is on the same line.
            print(prompt_string, end='', flush=True)
            
            # Initialize the key value to None.
            key = None
            
            # Keep looping until a key value has been retrieved from the queue.
            while key is None:
                key = key_queue.get()
            
            # Return the key value to the calling function.
            return key
    
    # Defines function to get user input with a prompt string and returns user input string.
    def get_input(self, prompt: str) -> str:
        """
        Clears any key presses waiting to be processed and gets user input from the console and returns it as a string.

        Args:
            prompt: A string representing the prompt to display to the user.

        Returns:
            A string representing the user's input.
        """
        
        # Loop to check if a key press is waiting to be processed.
        while msvcrt.kbhit():
            # Function to block a pending key press.
            msvcrt.getch()
        
        # Get input from user by asking prompt string from function parameter.
        user_input = input(prompt)
        
        # Return the user input value to the calling function.
        return user_input
    
    def get_mouse_button(self, prompt_string: str):
         # Create a new queue object to hold the mouse button value.
        mouse_queue = Queue()
        
        def on_click(x, y, button, pressed, mouse_queue=mouse_queue):
            if pressed:
                # Add the button to the queue when it is pressed.
                mouse_queue.put(button)
        
        with MouseListener(on_click=on_click):
            # Print the prompt string to the console.
            # Use flush=True to ensure that the message is printed immediately.
            # Use end='' to make sure that the next print statement is on the same line.
            print(prompt_string, end='', flush=True)
            
            # Initialize the key value to None.
            mouse_button = None
            
            # Keep looping until a key value has been retrieved from the queue.
            while mouse_button is None:
                mouse_button = mouse_queue.get()

            # Return the key value to the calling function.
            return mouse_button

