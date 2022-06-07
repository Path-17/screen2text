#!/usr/bin/python3

import subprocess
import os
from pynput.keyboard import Key, Listener, KeyCode
import time
from PIL import Image
import pytesseract
import pyperclip


    #    os.system("xclip -selection clipboard -t image/png -o > clip.png")

def on_press(key):
    print(type(key))
    if key == KeyCode.from_char('c'):
        time.sleep(1)
        subprocess.check_output("xclip -selection clipboard -t image/png -o > /tmp/clip.png", shell=True)
        result = pytesseract.image_to_string("/tmp/clip.png")
        pyperclip.copy(result)
        print(result)
        exit()

if __name__ == "__main__":

    subprocess.check_output(["flameshot", "gui"])
    
    with Listener(on_press=on_press) as listener:
        listener.join()

