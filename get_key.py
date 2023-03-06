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

keyboard_listener = None
key_input = None

def get_key(prompt_string):
    global key_input
    global keyboard_listener
    
    if keyboard_listener is None or not keyboard_listener.running:
        keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release, daemon=True)
        key_input = None
        keyboard_listener.start()
    
    key_input = None
    print(prompt_string, end="")
    
    while key_input is None:
        pass
    
    keyboard_listener.stop()
    keyboard_listener.join()
    
    print(key_input)
    
    return key_input
