# Import required libraries
import os # Required to run shell commands
from datetime import datetime # Required to get the current date and time
import time # Required to invoke delays in the script
import tts # Text to speech library

import led_strip_process # Import the processing library for sending instructions to the LEDs


def Start():
    tts.Speak("Loaded pattern lighting", speed="fast", wait=True) # Announce that the 'Pattern Lighting' app has finished opening.
    while True:
        print("Please enter a pattern")
        tts.Speak("Please enter a lighting pattern", speed="fast", wait=False) # Announce that the 'Pattern Lighting' app has finished opening.
        pattern_selection = input("Selection: ")
        if (pattern_selection == "knightrider"):
            led_strip_process.pattern_knightrider()
        elif (pattern_selection == "rainbow"):
            led_strip_process.pattern_rainbow()
        elif (pattern_selection == "randompixelstrobe"):
            led_strip_process.pattern_randompixelstrobe()
        elif (pattern_selection == "breathe"):
            led_strip_process.pattern_breate()
