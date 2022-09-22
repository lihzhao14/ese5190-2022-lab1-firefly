import time
import board
import busio
import neopixel
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_apds9960.apds9960 import APDS9960



#enable i2c
i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)

#enable sensors
apds.enable_proximity = True
apds.enable_color = True
apds.enable_gesture = True
apds.color_integration_time = 219

#LED
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

# Keyboard object
time.sleep(5)  # Sleep for a bit to avoid a race condition on some systems
kbd = Keyboard(usb_hid.devices)
kbd_layout = KeyboardLayoutUS(kbd) #use the US keyboard

paused = False

while True:
    #distance
    if not paused:
        distance=apds.proximity
        print('distance:{0}\n'.format(distance))
        if distance<50 and distance!=0:
            kbd_layout.write('ALERT\n')
            time.sleep(0.1)
            pixels.fill((0, 0, 0))
            time.sleep(0.1)
            pixels.fill((255, 0, 0))
        else:
            kbd_layout.write('SAFE\n')
            pixels.fill((0, 255, 0))

    #gesture
    gesture = apds.gesture()
    if not paused:
        if gesture == 0x01:
            pixels.fill((255, 255, 255))
            kbd_layout.write('CLEAR\n')
            kbd.send(Keycode.LEFT_CONTROL, Keycode.A)
            kbd.send(Keycode.BACKSPACE)

    if gesture == 0x02:
        kbd_layout.write('Interrupted\n')
        pixels.fill((0, 0, 255))
        paused = True

    if gesture == 0x03:
        kbd_layout.write('Continue\n')
        pixels.fill((0, 0, 255))
        paused = False

    time.sleep(1)