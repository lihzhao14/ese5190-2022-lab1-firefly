University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1  

    Lihong Zhao  
        LinkedIn: www.linkedin.com/in/lihong-zhao-a24789224  
    Tested on: Lenovo Legion 5 Pro 16" Laptop, Windows11 

## Introduction
RP2040 microcontroller and APDS9960 sensor board are used in this lab. There are two main results are presented:    
* The APDS9960 sensor was set up to make the LED on the RP2040 blink in response to the fireflies in the [video](https://www.youtube.com/watch?v=BtCGtaMrBXQ&t=413s), and the result is shown by **GIF 1**.  
* By understanding the CircuitPython HID Keyboard Library, a custom program was created and the result is shown by [**GIF 2**].  
### 1. Firefly Visualizer
<div align=center>
<img src="https://github.com/lihzhao14/ese5190-2022-lab1-firefly/blob/main/Image/3.2.gif" width="600">  
</div>

<p align="center">GIF 1</>

### 2. Custom Visualizer

In this section, the proximity sensing and color sensing of the ADPS9960 sensor are used as inputs.RP2040 is programmed to perform the following functions which are also shown as a digram in Figure 2:
* When the value of proxmity is less 50 and not equal yo 0, the LED on the RP2040 will flash with red light and "ALERT" will be typed on the screen. Otherwise, the LED will be on with green light and "SAFE" will be typed on the screen.
* If the user's finger moves upward, the LED on the RP2040 will be on with the combination color with red, green and blue. Also, "CLEAR" will be typed on the screen and all the words showing on the screen will be cleared off.
* If the user's finger moves downward, the LED on the RP2040 will be on with blue light and "Interrupt" will be typed on the screen. Meanwhile, the program will be interrupted.
* If the user's finger moves to the left, the LED on the RP2040 will be on with green light and "Continue" will be typed on the screen. The program will continue to run from the beginning.

<div align=center>
<img src="https://github.com/lihzhao14/ese5190-2022-lab1-firefly/blob/main/Image/4.4.gif" width="420">  
</div>

<p align="center">GIF 2</>

*** 
 
<div align=center>
<img src="https://github.com/lihzhao14/ese5190-2022-lab1-firefly/blob/main/Image/Digram%20of%20Coustom%20visualizer.png">  
</div>

<p align="center">Figure 1. Diagram of Custom Visualizer</>

***  

<div align=center>
<img src="https://github.com/lihzhao14/ese5190-2022-lab1-firefly/blob/main/Image/Diagram%20of%20embedded%20system%20for%20Custom%20Visualizer.png">  
</div>

<p align="center">Figure 2. Diagram of embedded system for Custom Visualizer</>
