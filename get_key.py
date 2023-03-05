from pynput import keyboard

def on_press(key):
    pass

def on_release(key):
    global key_input
    if key:
        try:
            key_input = key.char
            keyboard_listener.stop()
            
        except AttributeError:
            key_input = key.name
            keyboard_listener.stop()

keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
key_input = None

def get_key(prompt_string):
    global key_input
    
    print("Key to toggle autoclicker: ", end="")
    
    keyboard_listener.start()
    keyboard_listener.join()
    
    print(key_input)
    
    return key_input
