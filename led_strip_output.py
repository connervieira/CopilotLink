# ----- CONFIGURATION START -----
led_strip_length = 50 # This setting determines how many LEDs are on your light strip. This should be changed to match the number of LEDs on light strips installed in your car in order to ensure animations play correctly, and that Copilot Link doesn't need to performance unnecessary processing.

# ----- CONFIGURATION END -----
# Under normal usage, you shouldn't need to edit anything below the script configuration section. Use caution when making changes below.


import board, neopixel, sys, time, random

pixels = neopixel.NeoPixel(board.D18, led_strip_length) # Define the lightstrip, and how many LEDs to use on it.

# arg1, arg2, and arg3 will usually be used as r, g, and b colors respectively, but in some cases, they may also be used to provide additional information about patterns.
arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]
pattern = sys.argv[4]

arg1 = int(arg1)
arg2 = int(arg2)
arg3 = int(arg3)


# Define the LED pattern functions
def Rainbow(speed): # Define the function to cycle all of the LEDs through all the colors of the rainbow.
    color = [255, 0, 0] # The color starts as completely red. Changing this could break the script.
    while True:
        for x in range (0,254):
            pixels.fill((color[0], color[1], color[2])) # Set all pixels to the current color.
            color[1] = color[1] + 1
            time.sleep(1/speed)
        for x in range (0,254):
            pixels.fill((color[0], color[1], color[2])) # Set all pixels to the current color.
            color[0] = color[0] - 1
            time.sleep(1/speed)
        for x in range (0,254):
            pixels.fill((color[0], color[1], color[2])) # Set all pixels to the current color.
            color[2] = color[2] + 1
            time.sleep(1/speed)
        for x in range (0,254):
            pixels.fill((color[0], color[1], color[2])) # Set all pixels to the current color.
            color[1] = color[1] - 1
            time.sleep(1/speed)
        for x in range (0,254):
            pixels.fill((color[0], color[1], color[2])) # Set all pixels to the current color.
            color[0] = color[0] + 1
            time.sleep(1/speed)
        for x in range (0,254):
            pixels.fill((color[0], color[1], color[2])) # Set all pixels to the current color.
            color[2] = color[2] - 1
            time.sleep(1/speed)

def KnightRider(timer=0.01): # Define the function to bounce a single red pixel back and forth like KITT from Knight Rider.
    for x in range(0, len(pixels)-1):
        pixels.fill((0,0,0))
        pixels[x] = (255, 0, 0)
        time.sleep(timer)
    for x in range(0, len(pixels)-1):
        pixels.fill((0,0,0))
        pixels[len(pixels)-1-x] = (255, 0, 0)
        time.sleep(timer)

def RandomPixelStrobe(): # Define the function to repeatedly pick a random LED and change it to a random color.
    while True:
        pixels[random.randint(0, len(pixels)-1)] = (random.randint(0,255), random.randint(0, 255), random.randint(0,255))

def Breathe(delay=0.012): # Slowly pulse all of the LEDs on and off.

    red_increment = 2 # How much to increment red by each time the LEDs update
    green_increment = 2 # How much to increment green by each time the LEDs update
    blue_increment = 2 # How much to increment blue by each time the LEDs update

    pixels.fill((0, 0, 0)) # Start with all of the LEDs turned off.
    current_color = [0, 0, 0] # This is a placeholder variable that will be incremented to make the lights breathe.
    while True:
        for x in range(0, 100): # Increase the brightness 100 times
            current_color = [current_color[0] + red_increment, current_color[1] + green_increment, current_color[2] + blue_increment] # Increment the LEDs up in brightness
            pixels.fill((current_color[0], current_color[1], current_color[2])) # Update the LEDs
            time.sleep(delay) # Wait before continuing
        for x in range(0, 100): # Decrease the brightness 100 times
            current_color = [current_color[0] - red_increment, current_color[1] - green_increment, current_color[2] - blue_increment] # Increment the LEDs down in brightness
            pixels.fill((current_color[0], current_color[1], current_color[2])) # Update the LEDs
            time.sleep(delay) # Wait before continuing




if (pattern == None or pattern == "" or pattern == "x" or pattern == "X"): # Determine whether a pattern was supplied to the script.
    pixels.fill ([arg1, arg2, arg3]) # If no pattern was set, just set the pixels to the supplied color.
else:
    if (pattern == "knightrider"):
        KnightRider() # Play the Knight Rider effect.
    elif (pattern == "rainbow"):
        Rainbow(1000) # Play the Rainbow effect at high speed.
    elif (pattern == "randompixelstrobe"):
        RandomPixelStrobe() # Play the Random Pixel Strobe effect.
    elif (pattern == "breathe"):
        Breathe() # Play the Breathe effect.
    else:
        print("Unknown pattern")

