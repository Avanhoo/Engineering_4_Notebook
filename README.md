# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Launchpad](#launchpad)
* [IMU](#crash-avoidance)
* [Raspberry_Pi_Assignment_Template](#raspberry_pi_assignment_template)
* [Onshape_Assignment_Template](#onshape_assignment_template)


&nbsp;



## Launchpad

### Assignment Description

This is a 4-part assignment.

**Part I:** 
Make code for a countdown from 10 to 0 that prints in the serial monitor.

**Part II:** 
Make a red light flash each second of the countdown and have a green one turn on at launch.

**Part III:** 
Add a button that triggers the launch.

**Part IV:** 
Move a servo on liftoff as if it were the launch tower.

### Evidence 

**Part I:**

![Part 1 Proof](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/3e9009f1-002f-4a35-924e-69918b6b5b1c)

**Part II:**

![Part 2 Proof](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/6989a081-3cb4-4c9f-9207-1bd5c7cb4c68)


**Part III:**

![Part 3 Proof](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/2a900709-ec32-4b81-ab43-73f1254401d8)


**Part IV:**

![Part 4 Proof](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/42674451-f5ba-4e0f-91cf-3503e56eb447)



### Wiring

**Part I:** N/A

**Part II:**

![Wiring2](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/92c9e949-5b6b-40d4-9697-71a5da441b7d)

**Part III:**

![Wiring3](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/96f06c19-8941-4005-8546-8e5703e3a2ac)

**Part IV:**

![Wiring4](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/4a5ecc07-3685-4481-b139-b2c34f081762)

### Code

<details>
<summary><b>Part I</b></summary>
    
<p>
    
```python
# type: ignore
import board
import digitalio
from time import sleep

for i in range (10,0,-1): #start, stop, step; nice and clean
    print(i)
    sleep(1)
print("Liftoff")
    
```
</p>  
    
</details>

    
<details>
<summary><b>Part II</b></summary>
    
<p>
    
```python

# type: ignore
import board
import digitalio
from time import sleep

Rled = digitalio.DigitalInOut(board.GP2) # Fourth pin down, top left
Rled.direction = digitalio.Direction.OUTPUT
Gled = digitalio.DigitalInOut(board.GP0) # First pin, top left
Gled.direction = digitalio.Direction.OUTPUT


for i in range (10,0,-1): #start, stop, step; nice and clean
    print(i)
    Rled.value = True # Flash red
    sleep(.1)
    Rled.value = False
    sleep(.9)
print("Liftoff")
Gled.value = True
sleep(5)

```
</p>  
    
</details>


<details>
<summary><b>Part III</b></summary>
    
<p>
    
```python
# type: ignore
import board
from digitalio import Direction, DigitalInOut, Pull
from time import sleep

Rled = DigitalInOut(board.GP2) # Fourth pin down, top left
Rled.direction = Direction.OUTPUT
Gled = DigitalInOut(board.GP0) # First pin, top left
Gled.direction = Direction.OUTPUT
button = DigitalInOut(board.GP28) # 7th pin down, right side
button.direction = Direction.INPUT
button.pull = Pull.UP
launch = False
print("System Active")

while True:
    while button.value:
        sleep(.1)
    for i in range (10,-1,-1): #start, stop, step; nice and clean
        print("t: -" + str(i))
        Rled.value = True # Flash red
        sleep(.1)
        Rled.value = False
        sleep(.9)
        if not button.value: # Exits for loop and restarts program
            print("ABORT")
            break
        if i == 0:
            launch = True

    if launch: # Makes sure it only launches if the countdown is finished
        launch = False
        print("Liftoff")
        Gled.value = True
        sleep(5)
    sleep(.5)

```
</p>  
    
</details>

<details>
<summary><b>Part IV</b></summary>
    
<p>
    
```python

# type: ignore
import board
from digitalio import Direction, DigitalInOut, Pull
from time import sleep
import pwmio
from adafruit_motor import servo

Rled = DigitalInOut(board.GP2) # Fourth pin down, top left
Rled.direction = Direction.OUTPUT
Gled = DigitalInOut(board.GP0) # First pin, top left
Gled.direction = Direction.OUTPUT
button = DigitalInOut(board.GP28) # 7th pin down, right side
button.direction = Direction.INPUT
button.pull = Pull.UP
servo_pwm = pwmio.PWMOut(board.GP27, duty_cycle=2 ** 15, frequency=50)
servo = servo.Servo(servo_pwm, min_pulse=500, max_pulse=2500)


launch = False
print("System Active")


while True:
    

    while button.value:
        sleep(.1)
    servo.angle = 0 # Resets system
    Gled.value = False
    
    for i in range (10,0,-1): #start, stop, step; nice and clean
        print("t: -" + str(i))
        Rled.value = True # Flash red
        sleep(.2)
        Rled.value = False
        sleep(.8)
        if not button.value: # Exits for loop and restarts program
            print("ABORT")
            Rled.value = True
            sleep(1)
            for o in range (5): # Overcomplicated code to make the light flash on abort
                Rled.value = True
                sleep(.03)
                Rled.value = False
                sleep(.03)
            break # Exits the countdown for loop
        if i == 1: # Makes sure it only launches if the countdown is finished
            launch = True

    if launch: # Same as above
        launch = False
        print("Liftoff")
        for i in range (0,180,1): # Sweeps the servo from 0 to 180
            servo.angle = (i)
            sleep((1/60))
        Gled.value = True
        sleep(3)
    sleep(.5)

```
</p>  
    
</details>


### Reflection

**Part I:**
This was a very simple start, but I made sure to use a for loop to make the countdown as simple as possible.

**Part II:**
I had a bit of difficulty in getting the lights to turn on, which I realize was because I had the wrong pins. Since they aren't labled on the Pico I plugged one LED into ground and the other into pin 2 instead of 4, but after I fixed that it was pretty simple.

**Part III:**
The button gave me more trouble than it should have. This was due to confusion surrounding the pull up/down built into the pico. If you're pulling DOWN you need one 3.3V wire connected to the button and the other to your pin. If you're pulling UP you need a ground wire to the button and the other to your pin. I was doing the wrong direction of pull for my wiring as I didn't understand the difference between pull up and pull down.

**Part IV:**
Ironically the servo was the easiest part of this whole assignment. We used the circuitpython motor library which made it super simple, and I decided to touch up the code so that it would loop properly. I did decide to do the spicy version again, which I did by replacing the sleeps I used to make the light blink with for loops that swept the servo and slept at the same time.



## Crash Avoidance

### Assignment Description

We need to make a system using an IMU that displays angular data on a little OLED screen and flashes a light if the device is tilted more than 90°.\
For the spicy section we need to use an altimeter to have the warning light turn off when you're 3m above ground level.

### Evidence 

**Part I:**

![gyro_1_vid](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/c8cdfe38-a2d1-4359-9298-5684fe0bc824)

**Part II:**

![Look at the buffoon dance](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/8f8c0cf4-8fcd-43dc-b8a7-4cd68fa62980)

**Part III:**

![This file was smaller as a video](images/imu_3.gif)

**Spicy**

![Gyro_S](images/imu_4.gif)

### Wiring

**Part I:**

![Gyro_1](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/eac6b7ca-f805-4ee6-92fa-efcd658d93de)

**Part II:**

![Gyro_2](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/bbb2185f-89a7-42c4-b125-2aba24506d8c)

**Part III:**

![Gyro_3](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/63233c34-0b0c-46d4-a388-86f5b1bf732c)

**Spicy**

![Gyro_S](images/imu_4.gif)

### Code

<details>
<summary><b>Part I</b></summary>
    
<p>
    
```python

import board
import busio
import adafruit_mpu6050
from time import sleep

sda_pin = board.GP16
scl_pin = board.GP17
i2c = busio.I2C(scl_pin, sda_pin)
imu = adafruit_mpu6050.MPU6050(i2c)
x = 0
y = 0
z = 0

delay = .1

sleep(delay)

while True:
    print(f"Accel: {round(imu.acceleration[0]-.6,1)}, {round(imu.acceleration[1]+.2,1)}, {round(imu.acceleration[2],1)}")
    sleep(delay)

```
</p>  
    
</details>

<details>
<summary><b>Part II</b></summary>
    
<p>
    
```python

import board
import busio
import adafruit_mpu6050
import digitalio
from time import sleep

led = digitalio.DigitalInOut(board.GP3)
led.direction = digitalio.Direction.OUTPUT
sda_pin = board.GP16
scl_pin = board.GP17
i2c = busio.I2C(scl_pin, sda_pin)
imu = adafruit_mpu6050.MPU6050(i2c)
x = 0
y = 0
z = 0

delay = .1

sleep(delay)

while True:
    print(f"Accel: {round(imu.acceleration[0]-.6,1)}, {round(imu.acceleration[1]+.2,1)}, {round(imu.acceleration[2],1)}")
    if abs(imu.acceleration[0]-.6) > 9.3 or abs(imu.acceleration[1]+.2) > 9.3:
        led.value = True
    else:
        led.value = False
    sleep(delay)

```
</p>  
    
</details>

<details>
<summary><b>Part III</b></summary>
    
<p>
    
```python

import board
import busio
import adafruit_mpu6050
import digitalio
import terminalio
import displayio
from time import sleep
import adafruit_displayio_ssd1306
from adafruit_display_text import label
displayio.release_displays() # Necesarry or else the GPIO pin will still be seen as in use even after the code is done


i2c = busio.I2C(board.GP17, board.GP16)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP20) # Display
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
imu = adafruit_mpu6050.MPU6050(i2c, address=0x68) # Accelerometer

led = digitalio.DigitalInOut(board.GP3)
led.direction = digitalio.Direction.OUTPUT

delay = .1

sleep(delay)

while True:
    print(f"Accel: {round(imu.acceleration[0]-.6,1)}, {round(imu.acceleration[1]+.2,1)}, {round(imu.acceleration[2],1)}") # Uses fstring to place the rounded acceleration values into the string
    if abs(imu.acceleration[0]-.6) > 9.3 or abs(imu.acceleration[1]+.2) > 9.3 or (imu.acceleration[2] < 0): # Detects if the imu is tilted 90° in any direction
        led.value = True
    else:
        led.value = False

    splash = displayio.Group() # create the display group
    title = f"ANGULAR VELOCITY: \n X:{round(imu.gyro[0]-.6,3)} \n Y:{round(imu.gyro[1]+.2,3)} \n Z:{round(imu.gyro[2],3)}" # add title block to display group
    
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5) # the order of this command is (font, text, text color, and location)
    splash.append(text_area)    
    
    display.show(splash)# send display group to screen

    sleep(delay)

```
</p>  
    
</details>

<details>
<summary><b>Spicy</b></summary>
    
<p>
    
```python

import board
import busio
import adafruit_mpu6050
import adafruit_mpl3115a2
import digitalio
import terminalio
import displayio
from time import sleep
import adafruit_displayio_ssd1306
from adafruit_display_text import label
displayio.release_displays() # Necesarry or else the GPIO pin will still be seen as in use even after the code is done


i2c = busio.I2C(board.GP17, board.GP16)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP20) # Display
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
imu = adafruit_mpu6050.MPU6050(i2c, address=0x68) # Accelerometer
sensor = adafruit_mpl3115a2.MPL3115A2(i2c)
#sensor.sealevel_pressure = 1017


led = digitalio.DigitalInOut(board.GP3)
led.direction = digitalio.Direction.OUTPUT

delay = .1
baseAlt = sensor.altitude
Height = 0

sleep(delay)

while True:
    altitude = sensor.altitude
    if (baseAlt + 3 < altitude):
        Height = 1
    else:
        Height = 0
    print("Altitude: {0:0.3f} meters".format(altitude))
    print(f"Accel: {round(imu.acceleration[0]-.6,1)}, {round(imu.acceleration[1]+.2,1)}, {round(imu.acceleration[2],1)}") # Uses fstring to place the rounded acceleration values into the string
    if (abs(imu.acceleration[0]-.6) > 9.3 or abs(imu.acceleration[1]+.2) > 9.3 or (imu.acceleration[2] < 0)) and not (baseAlt + 3 < altitude): # Detects if the imu is tilted 90° in any direction
        led.value = True
    else:
        led.value = False

    splash = displayio.Group() # create the display group
    title = f"ANGULAR V: X:{round(imu.gyro[0]-.6,3)} \n           Y:{round(imu.gyro[1]+.2,3)} \n{Height}          Z:{round(imu.gyro[2],3)} \nAltitude: {altitude}" # add title block to display group
    
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5) # the order of this command is (font, text, text color, and location)
    splash.append(text_area)    
    
    display.show(splash)# send display group to screen

    sleep(delay)

```
</p>  
    
</details>

### Reflection

**Part I:**

I had used an IMU before for a previous assignment, but only for the rotation values. I thought I knew what I was doing but I was thinking of the accelerometer as a velocometer. I didn't realize that gravity existed because I was thinking that I was measuring the change in position and the IMU wasn't moving, but I was measuring the change in velocity, so gravity *did* exist.

**Part II:**

We used the IMU's acceleration value to do the list detection here instead of the angular gyroscope data it gives us, which turned out to be easier as you can use gravity as a reference. This means that the angle value will never drift and you don't have to worry too much about calibration. You just see if the x or y acceleration axes ever have an acceleration around 9.8 (gravity). 

**Part III:**

Adding a screen definitely made the wiring a mess. Code wise I had an issue because I forgot to put the displayio.release_displays() command at the start of my code, which essentially releases the GPIO i2c pins (as the name entails). After that got fixed it worked well, though I had to manually find the i2c adresses of the screen and imu this time, code below (credit to Mr. Miller). I'd also like to thank fstrings for existing, they make inserting variables into strings very easy, just use {*variable*}.
<details>
<summary><b>Click to Show</b></summary>
    
<p>
    
```python

import board
import time
import busio


sda_pin = board.GP4
scl_pin = board.GP5
i2c = busio.I2C(scl_pin, sda_pin)

while not i2c.try_lock():
    pass

try:
    while True:
        print(
            "I2C addresses found:",
            [hex(device_address) for device_address in i2c.scan()],
        )
        time.sleep(2)

finally:  # unlock the i2c bus when ctrl-c'ing out of the loop
    i2c.unlock()

```
</p>  
    
</details>

**Spicy**

I kinda lika da spicy. I'd been wanting to use a sensor like this for a personal project so this was a great learning opportunity.  The sensor can give temperature and pressure, the latter of which can be used to calculate altitude. It's a normal i2c board so getting it up and running is very easy, though it needs thorough calibration to give proper readings, so I just used it to give me the relative difference in altitude for this project by subtracting the current altitude from a set "base" altitude. This is one of the best use cases for a pressure-based altitude sensor like this, as the reading varies based on weather, season, and even if you blow on the sensor.

# Templates

## Raspberry_Pi_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Evidence 

Pictures / Gifs of your work should go here. You need to communicate what your thing does. 

### Wiring

This may not be applicable to all assignments. Anything where you wire something up, include the wiring diagram here. The diagram should be clear enough that I can recreate the wiring from scratch. 

### Code
Give me a link to your code. [Something like this](https://github.com/millerm22/Engineering_4_Notebook/blob/main/Raspberry_Pi/hello_world.py). Don't make me hunt through your folders, give me a nice link to click to take me there! Remember to **COMMENT YOUR CODE** if you want full credit. 

<details>
<summary><b>Click to Show</b></summary>
    
<p>
    
```python

```
</p>  
    
</details>

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;



## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link
[Hyperlink Text](https://en.wikipedia.org/wiki/Ural_Mountains)      

### Test Image

![Forest around mount Yamantau](images/Лес_вокруг_г.Ямантау.jpg)

### Test GIF

![Crying emoji evaporates](images/crying-emoji-dies.gif)


