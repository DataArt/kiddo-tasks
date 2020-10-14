import raccoon

while True:
    if(raccoon.inspect(0, 1) == 4):
        raccoon.go_down()
        break
    elif(raccoon.inspect(1, 0) == 1):
        raccoon.go_right()
    else:
        raccoon.go_down()