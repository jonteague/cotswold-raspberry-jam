#!/usr/bin/python3
import board
import neopixel
from random import randrange
import time


# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 3

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False,
                           pixel_order=ORDER)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r -> g -> b -> back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


def fade_in_out(wait):
    for j in range(255):
        pixels[0] = (j,0,0)
        pixels[1] = (0,j,0)
        pixels[2] = (0,0,j)
        pixels.show()
        time.sleep(wait)
    for j in range(254,0,-1):
        pixels[0] = (j,0,0)
        pixels[1] = (0,j,0)
        pixels[2] = (0,0,j)
        pixels.show()
        time.sleep(wait)


def random_leds(times, wait):
    for i in range(times):
        for j in range(num_pixels):
            pixels[j] = (randrange(256),randrange(256),randrange(256))
        pixels.show()
        time.sleep(wait)


while True:
    pixels.fill((255, 0, 0))
    pixels.show()
    time.sleep(1)

    pixels.fill((0, 255, 0))
    pixels.show()
    time.sleep(1)

    pixels.fill((0, 0, 255))
    pixels.show()
    time.sleep(1)

    pixels.fill((255, 255, 255))
    pixels.show()
    time.sleep(1)

    rainbow_cycle(0.02)

    fade_in_out(0.02)

    for i in range(num_pixels):
        pixels.fill((0,0,0))
        pixels[i] = (255, 0, 0)
        pixels.show()
        time.sleep(1)

    random_leds(100, 0.1)
