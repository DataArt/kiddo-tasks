import raccoon

direction = "left"
last_line = False

def turn(): 
    global direction
    if (direction == "left"):
        direction = "right"
    else:
        direction = "left"

def inspect_road():
    global direction
    global last_line
    if (direction == "left"):
        if (raccoon.inspect(-1, 0) == 1 or raccoon.inspect(-1, 0) == 3):
            raccoon.go_left()
            if (raccoon.inspect(-1, 0) == 0):
                turn()
        if (raccoon.inspect(0, -1) == 4):
            raccoon.go_up()
            last_line = True
        if (raccoon.inspect(0, -1) == 1):
            raccoon.go_up()
        
    else:
        if (raccoon.inspect(1, 0) == 1 or raccoon.inspect(1, 0) == 3):
            raccoon.go_right()
        if (raccoon.inspect(1, 0) == 0):
            turn()

while True:
    if (last_line == True):
        break
    elif (raccoon.inspect(-1, 0) == 0 and raccoon.inspect(1, 0) == 0):
        raccoon.go_up()
    else:
        inspect_road()
        