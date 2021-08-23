import board, neopixel, sys

pixels = neopixel.NeoPixel(board.D18, 100) # Define the lightstrip, and how many LEDs to use on it.

r, g, b = tuple (map (int, sys.argv [1:]))
r = int(r)
g = int(g)
b = int(b)
pixels.fill ([r, g, b]) # Set the pixels to the desired color
