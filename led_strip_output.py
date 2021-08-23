# ----- CONFIGURATION START -----
led_strip_length = 50 # This setting determines how many LEDs are on your light strip. This should be changed to match the number of LEDs on light strips installed in your car in order to ensure animations play correctly, and that Copilot Link doesn't need to performance unnecessary processing.

# ----- CONFIGURATION END -----
# Under normal usage, you shouldn't need to edit anything below the script configuration section. Use caution when making changes below.


import board, neopixel, sys, time

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

def KnightRider(): # Define the function to bounce a single red pixel back and forth like KITT from Knight Rider.
    for x in range(0, len(pixels)-1):
        pixels.fill((0,0,0))
        pixels[x] = (255, 0, 0)
        time.sleep(timer)
    for x in range(0, len(pixels)-1):
        pixels.fill((0,0,0))
        pixels[len(pixels)-1-x] = (255, 0, 0)
        time.sleep(timer)

def RandomPixels():
    while True:
        pixels[random.randint(0, len(pixels)-1)] = (255, 255, 255)
        time.sleep(random.uniform(0, 1))
        pixels.fill((0,0,0))



if (pattern == None or pattern == ""): # Determine whether a pattern was supplied to the script.
    pixels.fill ([arg1, arg2, arg3]) # If no pattern was set, just set the pixels to the supplied color.
else:
    if (pattern == "knightrider"):
        KnightRider() # Play the Knight Rider effect.
    elif (pattern == "rainbow"):
        Rainbow(1000) # Play the Rainbow effect at high speed.

