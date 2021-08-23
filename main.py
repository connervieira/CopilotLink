# Copilot Link
# V0LT
# Version 0.1


# ----- Configuration Start -----

# ----- Configuration End -----


# Import required libraries
from os.path import exists # Required to check if files exist
import os # Required to run shell commands
from datetime import datetime # Required to get the current date and time
import time # Required to invoke delays in the script


# Import apps
import announce_time # App to announce the current time in 15 second intervals.
import static_lighting # App to set connected LED strips to a static color.

# Import outputs
import speech # Pre-recorded speech library
import tts # Text to speech library




# Initial start up sequence. This is mainly to alert the user that Copilot is starting, since most people probably won't have Copilot connected to a display.
tts.Speak("Loading Copilot Link", speed="fast", wait=True)
tts.Speak("Loading complete", speed="fast", wait=True)


while True:
    os.system("clear")
    tts.Speak("Main menu. Please select an option.", speed="fast", wait=False)
    print("Please select an option.")
    print("0. List options verbally")
    print("1. List apps")
    print("2. List supported inputs")
    print("3. List supported outputs")
    i = int(input("Selection: "))

    tts.Speak("Selected " + str(i))
    os.system("clear")

    if (i == 0): # Read options
        print("Reading options")
        tts.Speak("Option 0. Reed options. Option 1. List apps. Option 2. List supported inputs. Option 3. List supported outputs.", speed="fast", wait=True) # List out the options verbally. Please note that "read" is intentionally misspelled as "reed" in order to get text-to-speech to pronounce it correctly.



    elif (i == 1): # Open apps menu
        tts.Speak("Apps menu. Please select an option.", speed="fast", wait=False)
        print("Please select an app")
        print("0. List apps verbally")
        print("1. Announce time")
        print("2. Static lighting")
        i = int(input("Selection: "))

        tts.Speak("Selected " + str(i))
        os.system("clear")
        if (i == 0):
            print("Listing apps")
            tts.Speak("Option 0. List apps. Option 1. Announce time", speed="fast", wait=True) # List out the apps verbally.
        elif (i == 1):
            tts.Speak("Loading announce time app")
            announcetime.Start()
        elif (i == 2):
            tts.Speak("Lighting apps menu. Please select an option.", speed="fast", wait=False)
            print("Please select a lighting app")
            print("0. List lighting apps")
            print("1. Static lighting")
            i = int(input("Selection: "))
            tts.Speak("Selected " + str(i))
            os.system("clear")

            if (i == 0):
                print("Listing lighting apps")
                tts.Speak("Option 0. List lighting apps. Option 1. Static lighting", speed="fast", wait=True) # List out the lighting apps verbally.
            elif (i == 1):
                static_lighting.Start()
            else:
                print("Error: Invalid option.")
                tts.Speak("Error, invalid option.", speed="fast", wait=True)
                
        else:
            print("Error: Invalid option.")
            tts.Speak("Error, invalid option.", speed="fast", wait=True)
        


    elif (i == 2): # Open inputs menu
        print("Not yet implemented")
        tts.Speak("Not yet implemented.", speed="fast", wait=True)



    elif (i == 3): # Open outputs menu
        print("Not yet implemented")
        tts.Speak("Not yet implemented.", speed="fast", wait=True)



    else: # Invalid selection
        print("Error: Invalid option.")
        tts.Speak("Error, invalid option.", speed="fast", wait=True)
