import os

def set_color (r: int, g: int, b: int):
    os.system (f"sudo python3 led_strip_output.py {r} {g} {b}")

def off():
    os.system (f"sudo python3 led_strip_output.py 0 0 0")
