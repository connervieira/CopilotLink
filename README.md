# Copilot Link

A platform that allows various sensors and output devices in a car to communicate with each other.

**Note:** Copilot Link is still in very early development, and everything is subject to change. At the moment, Copilot Link serves more as a proof of concept, and some of the features you see listed here might not be currently implemented. Always use reasonable judgement, and don't trust Copilot with safety critical tasks.


## Description

Copilot Link is a platform to allow drivers to become better connected to their cars. As a driver, you're used to receiving information from your car in various ways. Despite the fact that your car is a massively complex system of interconnected parts, the feedback you can receive from it is relatively small. The standard ways your car gives you feedback is through the steering, brake pedal, and dashboard, but this is significantly limiting.

This is where Copilot Link steps in.

Copilot Link strives to be a a single platform to connect various devices in your car together using inexpensive hardware. Unlike other software, Copilot doesn't want to disconnect you from driving. Instead of being designed around sending you notifications from your phone and playing your music, Copilot is your driving sidekick, and provides you with the information you need to be a more aware and focused driver.

That's not to say that Copilot can't be fun. While it's main purpose is to assist in driving, it can also be used to make your car do new and entertaining things, like controlling music and lighting systems to create light shows!

## Examples

Here are various usage examples of how Copilot Link could increase your level of awareness as a driver.

- Instead of having to glance down at the speedometer, Copilot could verbally announce your current speed over your car's sound system. Without drawing your eyes away from the road, you'll never end up driving faster than you mean to on the freeway.
- Copilot could read temperature data from your car's OBD II port, and use RGB light strips to keep you informed using your peripheral vision, allowing you to make informed decisions about driving in a performance context without having to look away from the track. As the light strips transition from green, to orange, to red, you'll know exactly how hard you're pushing the car.


## Features

### Open

Copilot Link is completely open and freely modifiable. Anyone who wants to add support for their custom set up is free to do so.

### Privacy

Copilot is completely privacy respecting and has absolutely no analytics built in.

### Offline

Copilot itself can run completely offline, meaning you aren't tethered to anywhere in specific. If your car can go somewhere, Copilot can come with it.

### Inexpensive

Copilot is designed to be used with inexpensive, generic parts. This allows you to connect plenty of sensors and output devices without having to spend hundreds of dollars.

### Low Power

Copilot is designed to run on a Raspberry Pi and other low-power-draw components. This makes it easy to power all of your Copilot hardware using auxiliary power ports already installed in your car.

### Informative

Copilot is designed to provide you with information in ways that don't distract you. Instead of having your phone on the dashboard, drawing your eyes away from the road, Copilot provides you with information in ways that make you a more informed driver, not a more distracted on.

### Fun

Copilot isn't just designed in a performance and safety context. There's also plenty of ways to use Copilot to enhance your car in entertaining ways, like playing light shows and music.


## Hardware

In the future. I plan on building a dedicated product to run Copilot Link using the hardware below. However, for now, you can still try to assemble it yourself. While I don't provide a tutorial based on it's complexity, I've tried to link to external tutorials when applicable.

Copilot Link is intentionally very modular, meaning there are very few concrete hardware requirements. However, this is a recommended parts list designed around making you more connected to your car without wasting money unnecessarily. The parts you use with Copilot Link is entirely dependent on what you want to do with it.

**Note**: This isn't intended to be a concrete parts list. Instead, is a general list to demonstrate the affordability of hardware compatible Copilot Link. You should ensure that the products you get are compatible with each other yourself before making any purchases.

1. Raspberry Pi 3B+
    - $30
2. Raspberry Pi power supply
    - $10
3. USB keyboard
    - $10
4. OBD ELM327 reader
    - $10
5. 3.5mm stereo jack cable
    - $8
6. RGB LED light strip (WS2812B)
    - $10
7. Wiring parts to connect Raspberry Pi and LEDs
    - $30
    - <https://www.thegeekpub.com/15990/wiring-ws2812b-addressable-leds-to-the-raspbery-pi/>


## Inputs

This section lists the inputs supported by Copilot Link (or inputs planned to be supported).

### Keyboard

This is the main input method for Copilot Link.

### OBD II (Planned)

OBD stands for On Board Diagnostics, and is the standard that all modern vehicles use to communicate with diagnostic devices. As long as your car is relatively modern, there's almost certainly a port under your dashboard on the driver side that allows you to get information from you car, including RPM, vehicle speed, and various temperature sensors.


## Outputs

This section lists the output methods currently supported by Copilot Link (or output methods planned to be supported).

### Audio: Text To Speech

Copilot can connect to your car's sound system and communicate information using text-to-speech.

### Audio: Prerecorded Speech

Copilot can connect to your car's sound system and communicate information using pre-recorded vocal samples.

### Visual: External Display/Aftermarket Stereo Unit

Copilot is based on a Raspberry Pi, which means it can easily display information using HDMI to an external display or the screen of an aftermarket stereo unit.

### Visual: RGB Lights (Neopixel compatible devices)

Copilot can communicate with RGB LED lights to display information through the peripheral vision of the driver and passengers.


## Applications

This section lists the applications currently built into Copilot Link.

### Announce Time

This app will use your car's sound system to announce the current time in 15 second intervals. In a rush? Use this app to keep your mind at easy without feeling pressured to look away from the road to check a clock.

### Static Lights

This app allows you to set the RGB light strips in your car to a static color. Whether you want to illuminate your car's interior to find something, or you just want some ambient lighting while sitting in a parking lot, this app eliminates the need for a dedicated RGB controller, and decreases the complexity of wiring for your car's interior lighting system.
