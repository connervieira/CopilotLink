import os

def set_color (r: int, g: int, b: int): # Sets all LEDs to a single color.
    os.system (f"sudo python3 led_strip_output.py {r} {g} {b} X")

def off(): # Turn off all LEDs
    os.system (f"sudo python3 led_strip_output.py 0 0 0 X")

def pattern_knightrider(): # Play the KITT Knight Rider pattern
    os.system (f"sudo python3 led_strip_output.py 0 0 0 knightrider")

def pattern_rainbow(): # Cycle all of the LEDs through all the colors of the rainbow
    os.system (f"sudo python3 led_strip_output.py 0 0 0 'rainbow'")

def pattern_randompixelstrobe():
    os.system (f"sudo python3 led_strip_output.py 0 0 0 'randompixelstrobe'")

def pattern_breathe():
    os.system (f"sudo python3 led_strip_output.py 0 0 0 'breathe'")
