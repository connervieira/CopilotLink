# Documentation

**Note**: This file is currently somewhat of a placeholder. These instructions are not complete, and are not thorough by any means. You're welcome to try to follow them, but expect to encounter issues.

## Installation/Setup
### Required
Steps in this section are required, and should be completed to ensure Copilot Link functions properly.

1. Download Copilot Link. You can either download the stable version from the V0LT website, or the development version from Github with the following command.
    - `git clone https://github.com/connervieira/CopilotLink`
2 Install 'playsound' Python library
    - `pip3 install playsound`
3. Install 'pygobject' Python library
    - `pip3 install pygobject`
4. Install 'obd' Python library
    - `pip3 install obd`
5. Download or compile Mycroft mimic, and place it at /bin/mimic.
    - <https://github.com/MycroftAI/mimic1>
    - If for some reason you don't want to place mimic at /bin/mimic, you can modify the file path in `tts.py` to match its location.
6. Change into the CopilotLink directory.
    - `cd CopilotLink`

### Recommended

Steps in this section are recommended. You might be able to get away with not completing them but you might not be able to use certain features of Copilot Link. If you you encounter errors, try working through these steps.

- [ ] Install required audio drivers to play sound through the audio jack of the Raspberry Pi.
- [ ] Install bluetooth packages on Linux. This is required to communicate with Bluetooth devices like OBD II readers and sensors.
    - `sudo apt-get install bluetooth bluez-utils blueman`
