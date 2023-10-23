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