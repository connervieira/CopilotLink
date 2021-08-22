# Pre-Recorded Speech Output


# ----- Configuration Start -----
resources_path = "./resources/sounds/default/vocals/" # This is the root path of the vocal sounds resources folder that you'd like to use. An absolute path is recommended for sake of reliability, but relative paths can be used as well.

# ----- Configuration End -----


from playsound import playsound # Required to play audio
from os.path import exists


def PlaySpeech(phrase):
    if (exists(resources_path + phrase + ".mp3") == True): # Check to make sure the desired vocal sound effect file actually exists.
        playsound(resources_path + phrase + ".mp3") # Play the vocal sound effect.
    else:
        print("Prerecorded Speech Output Error: The desired phrase, " + phrase + ", does not exist in the resources folder.")
