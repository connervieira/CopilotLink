# Import required libraries
import os # Required to run shell commands
from datetime import datetime # Required to get the current date and time
import time # Required to invoke delays in the script
import tts # Text to speech library

import led_strip_process # Import the processing library for sending instructions to the LEDs


# Define all of the static colors that the LEDs can be.
color_settings = {
    "off": [0, 0, 0],
    "white": [255, 255, 255],
    "red": [255, 0, 0],
    "green": [0, 255, 0],
    "blue": [0, 0, 255],
    "yellow": [255, 255, 0],
    "cyan": [0, 255, 255],
    "magenta": [255, 0, 255],
    "purple": [150, 0, 255],
    "pink": [255, 0, 175],
    "aqua": [0, 255, 90],
    "orange": [255, 140, 0]
}


def Start():
    tts.Speak("Loaded static lighting", speed="fast", wait=True) # Announce that the 'Lighting' app has finished opening.
    while True:
        print("Please enter a color")
        #tts.Speak("Please enter a color", speed="fast", wait=False) # Announce that the 'Lighting' app has finished opening.
        color_selection = input("Selection: ")
        led_strip_process.set_color(color_settings[color_selection][0], color_settings[color_selection][1], color_settings[color_selection][2])

Start()
