#!/usr/bin/python3
import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 3, auto_write=False)

pixels[0] = (255, 0, 0)
pixels[1] = (0, 255, 0)
pixels[2] = (0, 0, 255)
pixels.show()

time.sleep(2)

pixels.fill((0, 0, 0))
pixels.show()
