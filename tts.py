# Pre-Recorded Speech Output


# ----- Configuration Start -----
mimic_path = "/bin/mimic" # This is the path to the mimic executable. An absolute path is recommended for sake of reliability, but relative paths can be used as well.

# ----- Configuration End -----


from os.path import exists
import os
import subprocess

def Speak(phrase, wait=True, speed="fast"):
    if (exists(mimic_path) == True): # Check to make sure the mimic executable actually exists.
        if (speed == "fast"):
            if (wait == True):
                subprocess.call(mimic_path + " --setf duration_stretch=0.6 -t '" + phrase + "'", shell=True) # Run the command to have mimic speak the entered phrase quickly.
            else:
                subprocess.call(mimic_path + " --setf duration_stretch=0.6 -t '" + phrase + "' &", shell=True) # Run the command to have mimic speak the entered phrase quickly.
                
        elif (speed == "slow"):
            if (wait == True):
                subprocess.call(mimic_path + " --setf duration_stretch=1.3 -t '" + phrase + "'", shell=True) # Run the command to have mimic speak the entered phrase slowly.
            else:
                subprocess.call(mimic_path + " --setf duration_stretch=1.3 -t '" + phrase + "' &", shell=True) # Run the command to have mimic speak the entered phrase slowly.
        else:
            if (wait == True):
                subprocess.call(mimic_path + " --setf duration_stretch=1.0 -t '" + phrase + "'", shell=True) # Run the command to have mimic speak the entered phrase at a normal pace.
            else:
                subprocess.call(mimic_path + " --setf duration_stretch=1.0 -t '" + phrase + "' &", shell=True) # Run the command to have mimic speak the entered phrase at a normal pace.
    else:
        print("Text To Speech Output Error: The mimic executable path does not exist.")
