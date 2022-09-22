import time
import board
import busio
import neopixel
from adafruit_apds9960.apds9960 import APDS9960

i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_color = True
apds.enable_gesture = True
apds.color_integration_time = 219
apds.rotation = 270 # 270 for CLUE
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)


BRIGHTNESS_MARGIN = 512
past_brightness = -1
while True:
   if apds.color_data_ready:
      r, g, b, c = apds.color_data
      print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
      brightness = c
      if past_brightness == -1: past_brightness = brightness
      delta = brightness - past_brightness
      if delta > BRIGHTNESS_MARGIN:
         past_brightness = brightness
         print("light's up")
         pixels.fill((255, 0, 0))
      if delta < -BRIGHTNESS_MARGIN:
         past_brightness = brightness
         print("light's down")
         pixels.fill((0, 0, 0))