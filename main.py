import subprocess
import requests
import os
from pynput.keyboard import Key, Listener, KeyCode

# Detect if connected to bridge
wifi_name = open(f'{os.path.expanduser("~")}/wifi/name.txt', 'r').read()


def wifi_on():
    return wifi_name in subprocess.check_output("netsh wlan show interfaces").decode("utf-8")


def reconnect():
    print("Hotkey pressed")
    # Send POST to log in
    #if wifi_on():
        #requests.post("https://www.btwifi.com:8443", ...)


if wifi_on():  # Connected
    r = requests.get("https://www.btwifi.com:8443")
    if "bthub-loginForm__toggleButton" in r.text:
        print("Logged out")
        reconnect()
    else:
        print("Logged in")

# Have to wait to be logged out of WiFi to continue...
# Implement hotkey to attempt reconnection on press

combo = (Key.shift, KeyCode.from_char("¬"))
current = set()


def on_press(key):
    if key in combo:
        current.add(key)
        if set(combo) == current:
            reconnect()


def on_release(key):
    if key == Key.esc:
        return False


with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
