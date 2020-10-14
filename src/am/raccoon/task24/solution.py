import raccoon

direction = 'forward'
def go_horizontal():
    if (direction == 'forward'):
        raccoon.go_right()
    else:
        raccoon.go_left()
        
def turn_around():
    global direction
    if (direction == 'forward'):
        direction = 'backward'
    else:
        direction = 'forward'
        
def inspect_forward():
    if (direction == 'forward'):
        return raccoon.inspect(1, 0)
    else:
        return raccoon.inspect(-1, 0)

inspectRight = raccoon.inspect(1,0)

while True:
    if(raccoon.inspect(1, 0) == 4):
        raccoon.go_right()
        break
    elif(raccoon.inspect(0, 1) == 1):
        raccoon.go_down()
        direction = 'forward'
    else:
        if (inspect_forward() == 0):
            turn_around()
        go_horizontal()