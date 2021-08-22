# Pre-Recorded Speech Output


# ----- Configuration Start -----
mimic_path = "/bin/mimic" # This is the path to the mimic executable. An absolute path is recommended for sake of reliability, but relative paths can be used as well.

# ----- Configuration End -----


from os.path import exists
import os

def Speak(phrase):
    if (exists(mimic_path) == True): # Check to make sure the mimic executable actually exists.
        os.system(mimic_path + " -t '" + phrase + "'") # Run the command to have mimic speak the entered phrase.
    else:
        print("Text To Speech Output Error: The mimic executable path does not exist.")
