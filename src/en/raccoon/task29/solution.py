import raccoon

raccoon.go_left(3)
raccoon.go_right(3)

def find_way():
    raccoon.go_right(3)
    if (raccoon.inspect(0, -1) == 0):
        raccoon.go_down(3)
    else:
        raccoon.go_up(3)
    

if (raccoon.inspect(1, 0) == 1):
    raccoon.go_right(3)
elif (raccoon.inspect(0, -1) == 1):
    raccoon.go_up(3)
    find_way()
elif (raccoon.inspect(0, 1) == 1):
    raccoon.go_down(3)
    find_way()


    