# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Launchpad](#launchpad)
* [IMU](#crash-avoidance)
* [FEA Part 1](#beam-design-fea-1)
* [FEA Part 2](#fea-part-2)
* [FEA Part 3](#beam-iteration-fea-3)
* [Landing Area Part 1](#landing-area-1)
* [Landing Area Part 2](#landing-area-2)
* [Morse code 1](#morse-code-1)
* [Morse code 2](#morse-code-2)
* [Data Part 1](#data-part-1)
* [Data Part 2](#data-part-2)



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
This was a very simple start, but I made sure to use a for loop to make the countdown as simple as possible. J'ai oublier que j'ai besoin d'importre le bibliothèque "temps", et parce que de la j'etais confus sur pourquoi mon code etait non fonctionnel. Ne oublier pas votre bibliothèques!

**Part II:**
I had a bit of difficulty in getting the lights to turn on, which I realize was because I had the wrong pins. Since they aren't labled on the Pico I plugged one LED into ground and the other into pin 2 instead of 4, but after I fixed that it was pretty simple

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

![Gyro_S](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/6b55ffa2-f0d4-4c28-a2d7-49bb55a2d2f4)

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
sensor = adafruit_mpl3115a2.MPL3115A2(i2c) # Altimeter
#sensor.sealevel_pressure = 1017


led = digitalio.DigitalInOut(board.GP3)
led.direction = digitalio.Direction.OUTPUT

delay = .1
baseAlt = sensor.altitude # base altitude your current position is measured against
Height = 0

sleep(delay)

while True:
    altitude = sensor.altitude
    if (baseAlt + 3 < altitude): # Checks if you're 3m above the starting point
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






# Onshape

## Beam Design (FEA 1)

### Assignment Description

In this assignment we have to create a beam supported on one end that can hold weight on the other (180cm long). The beam must weigh less than 13g and will be printed out of 100% infill PLA. Our design can't feature overhangs <45°, and the beam fails once it snaps or bends >35cm
### Part Link 

[Create a link to your Onshape document]([https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021](https://cvilleschools.onshape.com/documents/8bb0d31d162d28dc9f991ea0/w/fe1197780904e4d1d1386b24/e/ee044e03919576f44710a8b6?renderMode=0&uiState=651d6a0766bcfe34cbaa30f0))

### Part Image

![Afton Final](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/6d3b4032-9374-4efa-93fe-f57a97636bd7)
![Afton Final (1)](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/0f3b8bf1-6db1-4b09-9d50-988b8b6535c0)

### Reflection

The design constraints we were given for this challenge were hard. The base block of the beam weighs ~5g to begin with, so you effectively have 8g of material to use. This type of beam is called a cantilever beam, and there is a bit of information online on how to design one. The only problem is that all of the designs I could find had a slight tapering on the underside of the beam as it extended out, which we can't print as it would make the whole beam an overhang. So I had to use this idea of the beam getting smaller towards the end in a different manner. 

I decided to make it shrink down in height on the top so that the end would still be lighter, but the bottom was flat and printable. My design is a very simple idea, with my reasoning being that you need a strong section on both the bottom and top of the beam. The bottom part will hold the compression of the whole beam as it bends downwards, the top part would would help control the tension created on the top of the beam as it bends downwards. The middle support is intended to prevent it from folding in half, and I was scared that it would fail at the point where it attaches to the holding block, so I added some small supports to help distribute the load (at least that was the idea). This whole thing took an iteration or 2, but I found the loft tool to be helpful for my design (though you can't loft a sketch with a hollow center, so you need to use 2)., me, or your college admission committee!

&nbsp;



## FEA Part 2

### Assignment Description

Render and analyze force and deflection plots of your beam and think how to improve your design.

### Part Link 

[Onshape Document](https://cvilleschools.onshape.com/documents/8bb0d31d162d28dc9f991ea0/w/fe1197780904e4d1d1386b24/e/18919759dab88ab0bac8a0ae)

### Part Image

![273233689-d2153ce2-1e13-4d53-81cb-47b457737f58](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/ba88b0bb-dad4-497b-9ac8-c7a8b2dfb84b)
![273233701-79a6c5ea-4d05-41b5-95b8-409da07e9aa4](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/2ff2f48b-3a9e-4497-b1dc-5382f78ab6f3)

### Reflection

Me and Nick had 2 separate designs for our beams, but we decided to go with mine as Nick's broke the rules and couldn't even render. I designed this one from the start with a "shrink factor", which is a number where sf > 1 which governs how much the end of the part is scaled down compared to the base. I used a loft to connect the start and end, so that I can change the beam at any point through a single variable. The stress on the beam was concentrated at the base, so I'd like to reinforce it with filleted edges, and by lowering the shrink factor, as the end of the beam doesn't have much stress on it. This will allow me some extra material to further reinforce the base and add some extra supports to the top which go down the length of the beam, which has a lot of stress on it.



## Beam Iteration (FEA 3)

### Assignment Description

This is the iterative design phase, where we use Onshape simulations to find weaknesses in our designs and improve them.
### Part Link 

[Onshape Document](https://cvilleschools.onshape.com/documents/8bb0d31d162d28dc9f991ea0/w/fe1197780904e4d1d1386b24/e/18919759dab88ab0bac8a0ae)

The goblet / 𝛙(psi) beam

![Goblet](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/1dea0961-8fc8-444d-a727-18f4146a9d4d)



### Reflection

The original "lowercase i beam" design was relatively strong but it had quite a lot of stress along the top of the beam. 
![Old](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/91022632-27e8-4f47-86b0-a0aa97a1e9af)
(Stress is 4lbf in all pictures shown)

To try and reduce this I added supports on the sides of the top circle to try and hold some of the weight. This worked well at lowering the top stress to manageable levels, but the pressure was now concentrated at the base of the beam. 
![improve](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/601b4bc5-061d-4d29-9d17-27219209dce5)

I changed the "shrink factor" which made the end of the beam smaller to reduce weight as the middle and end of the beam don't have to bear much load and therefore shouldn't weigh much. This allowed me the extra material to fillet the base of the beam, which drastically improved the pressure, though there are still "hotspots" that have high stress.         (↓ in MPa)
![New](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/894ee2bd-8b38-4a8f-b8aa-c6d2e3f174ff)

&nbsp;

## Landing Area 1

### Assignment Description

Create a program that calculates the area of a triangle based on 3 input coordinates. It must use a function and take coordinates in an x,y format.
### Evidence 

![coordinates_proof](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/66d68321-f92c-436d-898e-0eb6e734dc82)

### Code


<details>
<summary><b>Click to Show</b></summary>
    
<p>
    
```python

# Triangle Are Solver - Afton Van Hooser
from time import sleep

x = 0
y = 1

def area(r1,r2,r3):
    c1 = [0,0]
    c2 = [0,0]
    c3 = [0,0]
    try:                    # Coordinate 1
        c1 = [int(o) for o in r1.split(",")] # Splits raw string: "1,2" into a string array: "1", "2", and turns each value into an int: 1,2
    except:
        print("Coordinate 1 Invalid, please enter in 'x,y' format")
        pass
    finally:

        try:                # Coordinate 2
            c2 = [int(o) for o in r2.split(",")]
        except:
            print("Coordinate 2 Invalid, please enter in 'x,y' format")
            pass
        finally:

            try:            # Coordinate 3
                c3 = [int(o) for o in r3.split(",")]
            except:
                print("Coordinate 3 Invalid, please enter in 'x,y' format")
                pass
            finally:
                A = (1/2)*abs(c1[x]*(c2[y] - c3[y]) + c2[x]*(c3[y] - c1[y]) + c3[x]*(c1[y] - c2[y])) # Easy plug and play equation for a triangle's area
                return A


while True:
    r1 = input("Coordinate 1: ")
    r2 = input("Coordinate 2: ")
    r3 = input("Coordinate 3: ")
    print(area(r1,r2,r3))
```
</p>  
    
</details>

### Reflection

The biggest challenge in this assignment was turning the raw coordinate input into usable numbers. At first I tried to do some intricate parsing of the input to check if it was valid and split it along the comma. I realized, though, that I could just use a try statement, which I could make run different paths depending on if the code worked properly or not. I then used some fancy operators to split the coordinates and turn them into integers in one line. To be honest I thought that the math for finding the area of the triangle, but thankfully River saved me from going down a pythagorean theory rabbit hole, and showed me a single equation that does some magic to spit out the area of any triangle.




## Landing Area 2

### Assignment Description

Graph the landing area on an OLED screen.

### Evidence 

![Landing_video](images/landing_video.gif)

### Wiring

![la2](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/e1d2d3ab-3cd8-428e-aeab-92ef1897f2a7)

### Code

<details>
<summary><b>Click to Show</b></summary>
    
<p>
    
```python

# Triangle Are Solver and Dispayer - Afton Van Hooser
import board
import busio
import terminalio
import displayio
from time import sleep
import adafruit_displayio_ssd1306
from adafruit_display_text import label
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle


displayio.release_displays() # Necesarry or else the GPIO pin will still be seen as in use even after the code is done

i2c = busio.I2C(board.GP17, board.GP16)

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP20) # Display
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

x = 0
y = 1

def qdisp(title): # Stands for quick display. Creates a function that runs all the lines nececarry to update the display in one line
    splash = displayio.Group() # create the display group
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5) # the order of this command is (font, text, text color, and location)
    splash.append(text_area)    
    display.show(splash)# send display group to screen

def qgraph(c1,c2,c3,A):
    scale = 1
    x0 = 64
    y0 = 32
    splash = displayio.Group()

    for i in range (1,7):
        scale = i
        if (abs(c1[x])*scale > 60) or (abs(c2[x])*scale > 60) or (abs(c3[x])*scale > 60):
            scale = i-1
            break

        elif (abs(c1[y])*scale > 30) or (abs(c2[y])*scale > 30) or (abs(c3[y])*scale > 30):
            scale = i-1
            break


    hline = Line(0,y0,128,y0, color=0xFFFF00)
    vline = Line(x0,0,x0,64, color=0xFFFF00)
    circle = Circle(x0, y0, 2*scale, outline=0xFFFF00)
    text = label.Label(terminalio.FONT, text=f"A={A}\n\n\n{scale}x", color=0xFFFF00, x=5, y=5)
    splash.append(hline) 
    splash.append(vline)
    splash.append(circle)
    splash.append(text)

    triangle = Triangle((c1[x])*scale+x0, (-c1[y])*scale+y0, (c2[x])*scale+x0, (-c2[y])*scale+y0, (c3[x])*scale+x0, (-c3[y])*scale+y0, outline=0xFFFF00)
    splash.append(triangle)

    display.show(splash)


def area():
    c1 = []
    c2 = []
    c3 = []

    while (c1 or c2 or c3) == []:
        r1 = input("Coordinate 1: ")
        try:                    # Coordinate 1
            c1 = [int(o) for o in r1.split(",")] # Splits raw string: "1,2" into a string array: "1", "2", and turns each value into an int: 1,2
            a = c1[0] + c1[1]
            qdisp(f"Coordinates: \n c1: {c1}")

            r2 = input("Coordinate 2: ")
            try:                # Coordinate 2
                c2 = [int(o) for o in r2.split(",")]
                qdisp(f"Coordinates: \n c1: {c1} \n c2: {c2}")

                r3 = input("Coordinate 3: ")
                try:            # Coordinate 3
                    c3 = [int(o) for o in r3.split(",")]
                    A = (1/2)*abs(c1[x]*(c2[y] - c3[y]) + c2[x]*(c3[y] - c1[y]) + c3[x]*(c1[y] - c2[y])) # Easy plug and play equation for a triangle's area
                    qdisp(f" c1: {c1} \n c2: {c2} \n c3: {c3} \nArea: {A}") # add title block to display group
                    sleep(1)
                    qgraph(c1,c2,c3,A)
                    return A

                except:
                    print("Invalid Coordinate 3 , please enter in 'x,y' format")
                    continue
                    
            except:
                print("Invalid Coordinate 2, please enter in 'x,y' format")
                continue
                
        except:
            print("Invalid Coordinate 1 , please enter in 'x,y' format")
            continue


while True:
    area()

```
</p>  
    
</details>

### Reflection

I used the OLED code from the previous assignment to print out the text, but I turned it into a function qdisp(). This made it much less cluttered in my area function. Graphing the landing area was the main part, though. There are libraries built to draw lines and shapes for you, and you can easily graph the triangles and lines from this, though where (0,0) would normally be on a graph is actually (64,32) on the display, as the coordinates start from the top left corner of the screen. I also decided to make it automatically scale the image to fit the screen. I used another function to do this, which checks the maximum scale which will fit the whole triangle on the screen by increasing the scale slowly until it doesn't fit. I was worried that this would give misleading senses of size, but I figured out that by also scaling the center circle I could make it clear that it was a zoomed-in image.

![1x](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/235cf540-48c6-48b2-8c7b-046b226508b4)
![2x](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/7ac77b14-9334-435d-a7d7-9bbf35c05cb5)
![6x](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/3b32bd19-04f1-481e-a58c-25aadcaa0b13)


## Morse code 1

### Assignment Description

Translate a user text input into morse code and print it out. Exit the program with "-q".

### Evidence 

![morse_1_proof](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/e95c4548-3c52-4013-9e71-edfc143e32a1)

### Wiring

N/A

### Code

<details>
<summary><b>Click to Show</b></summary>
    
<p>
    
```python

# Morse code translator - Afton Van Hooser
print("Morse code translator - Afton Van Hooser")
finalTxt = ""
char = 0
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ':'/'}

while True:
    rawTxt = input("Input Text: ").upper() # Takes input from user and capitalizes it
    finalTxt = ""

    if "-Q" in rawTxt: # Checks if user would like to exit
        exit()
    try:
        for char in range(len(rawTxt)): # Iterates through each character of the input text
            finalTxt += MORSE_CODE[rawTxt[char]] + " " # Translates and adds a space
    except:
        finalTxt = f'--Invalid input: "{rawTxt[char]}"' # Tells you if a character you typed was invalid

    print(finalTxt)

```
</p>  
    
</details>

### Reflection

This assignment was all string work, which I luckily have experience with from messing with a VFD. The main idea of the code is to iterate through each character of input and translate it, which can be done with a for loop and dictionary. I put this process in a try function as inputting anything like "$" which wasn't in the morse code dictionary would break the code. Lastly I made it quickly check if "-q" was sent, and subsequently exit the program through exit() if so.



## Morse code 2

### Assignment Description

Make the morse code translator flash out the morse code on an LED.

### Evidence 

![morse_2_proof](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/bc114db3-9a6c-46a0-8476-2ed248db746e)

### Wiring

This may not be applicable to all assignments. Anything where you wire something up, include the wiring diagram here. The diagram should be clear enough that I can recreate the wiring from scratch. 

### Code
[Source](https://github.com/Avanhoo/Engineering_4_Notebook/blob/main/raspberry-pi/morse.py)
<details>
<summary><b>Click to Show</b></summary>
    
<p>
    
```python

# Morse code translator - Afton Van Hooser
import board
import digitalio
from time import sleep

led = digitalio.DigitalInOut(board.GP3)
led.direction = digitalio.Direction.OUTPUT
print("Morse code translator - Afton Van Hooser")
finalTxt = ""
delay = .25
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ':'/'}

while True:
    rawTxt = input("Input Text: ").upper() # Takes input from user and capitalizes it
    finalTxt = ""

    if "-Q" in rawTxt: # Checks if user would like to exit
        exit()
    try:
        for char in range(len(rawTxt)): # Iterates through each character of the input text
            finalTxt += MORSE_CODE[rawTxt[char]] + " " # Translates and adds a space
    except:
        finalTxt = f'--Invalid input: "{rawTxt[char]}"' # Tells you if a character you typed was invalid

    print(finalTxt)

    for i in range(len(finalTxt)):# Flashing light loop
        if finalTxt[i] == ".": #    Dot
            led.value = True
            sleep(delay)
            led.value = False
        elif finalTxt[i] == "-": #  Dash
            led.value = True
            sleep(delay*3)
            led.value = False
        elif finalTxt[i] == " ": #  Between letters: inherent delay(1) + 1 + inherent delay(1) = 3 delay
            sleep(delay)
        if finalTxt[i] == "/": #    Between words: letter delay(3) + 1 + letter delay(3) = 7 delay
            sleep(delay)
        else:
            sleep(delay) #          Inherent Delay after every cycle
        

```
</p>  
    
</details>

### Reflection

The hardest part of this assignment was getting the proper delay times. I made my flashing light for loop have a delay after every loop. This made my life hard as I then had to account for this in my other delays. Instead of having the delay between letters sleep for 3 times the delay time (as is standard), I had it sleep for 1 times the delay time, as I had to account for the inherent delay of both the previous letter and of the delay itself. I spent a lot of time toiling away trying to logic out the proper delays, though I'm not sure if there's an easier alternative.
Also credit to Vince Jones for finding a fatal flaw in my code where the morse code output never reset and kept adding onto itself, I would have missed it if not for him.



## Data Part 1

### Assignment Description

Make a pi record accelerometer data in a spreadsheet. The pi must run on its own and create a .csv file.

### Evidence 

![data_1_proof](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/2e190c8e-52c3-4fe2-a905-3cd5f4e6e863)

#### Data Collected:

|Time (s)|X Acceleration|Y Acceleration|Z Acceleration|Tilted?|
|------|---------|---------|---------|---|
|7.96  |0.869095 |0.936133 |0.921768 |0  |
|8.266 |0.830788 |0.826    |0.864307 |0  |
|8.571 |0.842759 |0.857124 |0.859519 |0  |
|8.876 |0.873884 |0.847548 |0.828394 |0  |
|9.184 |1.03908  |1.08936  |1.40061  |0  |
|9.487 |-0.529119|-0.483629|-0.514753|0  |
|9.792 |-3.35907 |-3.71341 |-3.68228 |0  |
|10.099|-6.30393 |-5.9472  |-5.76284 |0  |
|10.402|-10.2376 |-9.91199 |-10.1275 |1  |
|10.708|-9.4547  |-9.46667 |-9.36372 |1  |
|11.015|-8.78672 |-8.81066 |-9.01656 |0  |
|11.324|0.577003 |0.234632 |0.612916 |0  |
|11.632|7.72609  |7.70454  |7.57047  |0  |
|11.939|9.79229  |9.85214  |9.72285  |0  |
|12.346|10.5704  |10.4938  |10.5656  |1  |


### Wiring

![data](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/e37473fb-28b9-4f45-8d2c-0144e1a53d64)

### Code

[Source](https://github.com/Avanhoo/Engineering_4_Notebook/blob/main/raspberry-pi/data_storage.py)
<details>
<summary><b>Click to Show</b></summary>
    
<p>
    
```python
import board
import busio
import adafruit_mpu6050
import digitalio
from time import sleep, monotonic

led = digitalio.DigitalInOut(board.GP3)
led.direction = digitalio.Direction.OUTPUT
sled = digitalio.DigitalInOut(board.LED)
sled.direction = digitalio.Direction.OUTPUT
sda_pin = board.GP16
scl_pin = board.GP17
i2c = busio.I2C(scl_pin, sda_pin)
imu = adafruit_mpu6050.MPU6050(i2c)

delay = .15
print(monotonic())
with open("/data.csv", "a") as datalog: # Opens / creates a file called data.csv to which the data is stored to
    while True:
        print(f"Accel: {round(imu.acceleration[0]-.6,1)}, {round(imu.acceleration[1]+.2,1)}, {round(imu.acceleration[2],1)}") # Prints the acceleration
        if abs(imu.acceleration[0]-.6) > 9.3 or abs(imu.acceleration[1]+.2) > 9.3:
            led.value = True
            tilt = 1
        else:
            led.value = False
            tilt = 0

        datalog.write(f"{monotonic()},{imu.acceleration[0]},{imu.acceleration[1]},{imu.acceleration[2]},{tilt}\n") # Writes the time, x, y, z acceleration, and if tilted to a file 
        datalog.flush()

        sled.value = True # Flashes onboard LED
        sleep(delay/2)
        sled.value = False
        sleep(delay/2)
```
</p>  
    
</details>

### Reflection

Picos can't read and write at the same time, so we had to use a boot file which set the mode based on a switch. This made testing a bit annoying as I didn't think you could see the terminal while the pico was on read only mode. This made debugging a little complicated, but the code worked well from the start. Just remember everything you want saved must be done in the "context" of the data.cvs file with the "open" function, and don't forget your new line or else the spreadsheet will all be in one row.



## Data part 2

### Assignment Description

Graph the acceleration and tilt data from the data.csv file.

### Evidence 

(Data & Graph Source)[https://docs.google.com/spreadsheets/d/1pX5fa3qjWEB4xVvUnExo1n80eGER_k2NqQpAeccUuP4/edit#gid=489656232]
![image](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/9ce4774b-397a-4959-a1cb-a275cf4800e6)

### Wiring

![data](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/82f199c5-03ea-4d08-aadd-346fb8843bf1)

### Code

<details>
<summary><b>Click to Show</b></summary>
    
<p>
    
```python
import board
import busio
import adafruit_mpu6050
import digitalio
from time import sleep, monotonic

led = digitalio.DigitalInOut(board.GP3)
led.direction = digitalio.Direction.OUTPUT
sled = digitalio.DigitalInOut(board.LED)
sled.direction = digitalio.Direction.OUTPUT
sda_pin = board.GP16
scl_pin = board.GP17
i2c = busio.I2C(scl_pin, sda_pin)
imu = adafruit_mpu6050.MPU6050(i2c)

delay = .15
print(monotonic())
with open("/data.csv", "a") as datalog:
    while True:
        print(f"Accel: {round(imu.acceleration[0]-.6,1)}, {round(imu.acceleration[1]+.2,1)}, {round(imu.acceleration[2],1)}") # Prints the acceleration
        if abs(imu.acceleration[0]-.6) > 9.3 or abs(imu.acceleration[1]+.2) > 9.3:
            led.value = True
            tilt = 1
        else:
            led.value = False
            tilt = 0

        datalog.write(f"{monotonic()},{imu.acceleration[0]},{imu.acceleration[1]},{imu.acceleration[2]},{tilt}\n") # Writes the time, x, y, z acceleration, and if tilted to a file 
        datalog.flush()

        sled.value = True # Flashes onboard LED
        sleep(delay/2)
        sled.value = False
        sleep(delay/2)

```
</p>  
    
</details>

### Reflection

I had some frustration regarding the pi and it wiping. For some reason it would completely wipe and reset to a blank slate whenever I unplugged it while the program was running. This is something that often happens when the Pico is shorted out, but I wasn't (to my knowledge) shorting it out. I could get it to not wipe about 50% of the time by turning off the switch on the battery connector before disconnecting the battery. The file was also sometimes filled with the ÿ character, which I assume was some weird corruption that occured when I unplugged it. I also fixed an error where it was saving the X acceleration to all 3 axis spots.










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


## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link
[Hyperlink Text](https://en.wikipedia.org/wiki/Ural_Mountains)      

### Test Image

![Forest around mount Yamantau](images/Лес_вокруг_г.Ямантау.jpg)

### Test GIF

![Crying emoji evaporates](images/crying-emoji-dies.gif)


