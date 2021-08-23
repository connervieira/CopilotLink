# Text-To-Speech Output


# ----- Configuration Start -----
mimic_path = "/bin/mimic" # This is the path to the mimic executable. An absolute path is recommended for sake of reliability, but relative paths can be used as well.
tts_enabled = False # This variable determines whether or not TTS will be used. False means that TTS will not be used.

# ----- Configuration End -----


from os.path import exists
import os

def Speak(phrase, wait=True, speed="fast"):
    if (exists(mimic_path) == True and tts_enabled == True): # Check to make sure the mimic executable actually exists, and that TTS is enabled.
        if (speed == "fast"):
            if (wait == True):
                os.system(mimic_path + " --setf duration_stretch=0.6 -t '" + phrase + "'") # Run the command to have mimic speak the entered phrase quickly.
            else:
                os.system(mimic_path + " --setf duration_stretch=0.6 -t '" + phrase + "' &") # Run the command to have mimic speak the entered phrase quickly.
                
        elif (speed == "slow"):
            if (wait == True):
                os.system(mimic_path + " --setf duration_stretch=1.3 -t '" + phrase + "'") # Run the command to have mimic speak the entered phrase slowly.
            else:
                os.system(mimic_path + " --setf duration_stretch=1.3 -t '" + phrase + "' &") # Run the command to have mimic speak the entered phrase slowly.
        else:
            if (wait == True):
                os.system(mimic_path + " --setf duration_stretch=1.0 -t '" + phrase + "'") # Run the command to have mimic speak the entered phrase at a normal pace.
            else:
                os.system(mimic_path + " --setf duration_stretch=1.0 -t '" + phrase + "' &") # Run the command to have mimic speak the entered phrase at a normal pace.
    else:
        print("Text To Speech Output Error: The mimic executable path does not exist.")
