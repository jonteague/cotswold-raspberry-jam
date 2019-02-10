import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 3)

pixels[0] = (255, 0, 0)
pixels[1] = (0, 255, 0)
pixels[2] = (0, 0, 255)
