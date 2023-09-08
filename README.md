# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Launchpad](#launchpad)
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

![Part I Proof](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/3e9009f1-002f-4a35-924e-69918b6b5b1c)

**Part II:**

**Part III:**

**Part IV:**

### Wiring

**Part I:** N/A

**Part II:**

![Wiring2](https://github.com/Avanhoo/Engineering_4_Notebook/assets/113116247/92c9e949-5b6b-40d4-9697-71a5da441b7d)

**Part III:**

**Part IV:**

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

    
```
</p>  
    
</details>


### Reflection

**Part I:**

This was a very simple start, but I made sure to use a for loop to make the countdown as simple as possible.

**Part II:**

I had a bit of difficulty in getting the lights to turn on, which I realize was because I had the wron pins. Since they aren't labled on the Pico I plugged one LED into ground and the other into pin 2 instead of 4, but after I fixed that it was pretty simple.

**Part III:**

**Part IV:**




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


