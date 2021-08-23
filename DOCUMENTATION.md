# Documentation

**Note**: This file is currently somewhat of a placeholder. These instructions are not complete, and are not thorough by any means. You're welcome to try to follow them, but expect to encounter issues.

## Installation/Setup

0. Set up your Raspberry Pi. No desktop environment is required, so a command line only installation is recommended for performance and reliability reasons.
1. Download Copilot Link. You can either download the stable version from the V0LT website, or the development version from GitHub with the following command.
    - `git clone https://github.com/connervieira/CopilotLink`
2. Install bluetooth packages on Linux. This is required to communicate with Bluetooth devices like OBD II readers and sensors.
    - `sudo apt-get install bluetooth bluez-utils blueman`
3. Install required Python libraries
    - `pip3 install playsound pygobject obd datetime time`
4. Install 'pygobject' Python library
    - `pip3 install pygobject`
5. Install 'obd' Python library
    - `pip3 install obd`
6. Download or compile Mycroft mimic, and place it at /bin/mimic.
    - <https://github.com/MycroftAI/mimic1>
    - If for some reason you don't want to place mimic at /bin/mimic, you can modify the file path in the configuration section of `tts.py` to match its location.
7. Optionally, install required audio software to play sound through the audio jack of the Raspberry Pi.
    - <https://projects-raspberry.com/getting-audio-out-working-on-the-raspberry-pi/>
9. Restart the Raspberry Pi to ensure all software and configuration changes are applied appropriately.
    - `sudo reboot`
10. After the Raspberry Pi finishes restarting, change into the CopilotLink directory.
    - `cd CopilotLink/`
11. Optionally, make any configurations you want in the 'configuration section' at the start of some of the scripts.
    - `vim main.py`
        - Configure main interface
    - `vim tts.py`
        - Configure Text-To-Speech system
    - `vim speech.py`
        - Configure pre-recoded speech system
12. Run Copilot Link to ensure that there are no errors.
    - `python3 main.py`
13. After Copilot Link loads, and you've confirmed that everything is working properly, close it by pressing *Ctrl+C*.
14. Physically connect any devices you'd like to use with Copilot, like a sound system or lighting system.
15. **INCOMPLETE (This step is not currently possible)**: Optionally, run the testing scripts for the hardware you have installed/connected in order to confirm everything is working properly.

### Recommended

Steps in this section are recommended. You might be able to get away with not completing them but you might not be able to use certain features of Copilot Link. If you you encounter errors, try working through these steps.

- [ ] Install required audio drivers to play sound through the audio jack of the Raspberry Pi.
- [ ] Install bluetooth packages on Linux. This is required to communicate with Bluetooth devices like OBD II readers and sensors.
    - `sudo apt-get install bluetooth bluez-utils blueman`
