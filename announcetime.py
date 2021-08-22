# Import required libraries
import speech # Pre-recorded speech library
from os.path import exists # Required to check if files exist
import os # Required to run shell commands
from datetime import datetime # Required to get the current date and time
import time # Required to invoke delays in the script
import tts # Text to speech library


announce_time_next_loop = True # This determines whether the current time will be announced on the next loop.

def AnnounceTime(): # Get the current time, parse it, and announce it.
    now = datetime.now() # Get the current time.
    current_hour = now.strftime("%H") # Get the hour from the current time.
    current_minute = now.strftime("%M") # Get the minute from the current time.
    current_second = now.strftime("%S") # Get the second from the current time.

    # Replace '00' with '0' to avoid confusing the text to speech algorithm.
    if (current_hour == "00"):
        current_hour = "0"
    if (current_minute == "00"):
        current_minute = "0"
    if (current_second == "00"):
        current_second = "0"

    tts.Speak(str(current_hour) + ":" + str(current_minute) + " and " + str(current_second) + " seconds", speed="fast", wait=True) # Speak the time out loud using text to speech.



def Start():
    tts.Speak("Loaded announce time app", speed="fast", wait=True) # Announce that the 'Announce Time' app has finished opening.

    # Announce the time when the app is first started.
    AnnounceTime()

    while True: # Run forever until cancelled.
        now = datetime.now() # Get the current time.
        current_hour = now.strftime("%H") # Get the hour from the current time.
        current_minute = now.strftime("%M") # Get the minute from the current time.
        current_second = now.strftime("%S") # Get the second from the current time.
        os.system("clear")
        print(current_hour + ":" + current_minute + ":" + current_second) # Display the current time on screen.

        if (current_second == "00" or current_second == "15" or current_second == "30" or current_second == "45"): # Only announce the current time in 15 second intervals.
            AnnounceTime() # Announce the current time.

        time.sleep(1) # Wait for 1 second, since we don't care about milliseconds
