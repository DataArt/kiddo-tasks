import raccoon

raccoon.go_down(8)
raccoon.go_right()

def search_and_destroy():
    destroyed = False
    for i in range(0, 16):
        if (raccoon.inspect(1, 0) == 2):
            raccoon.wait(2)
            raccoon.go_right()
            raccoon.set_mine()
            raccoon.go_left()
            raccoon.wait(13)
            destroyed = True
    
    if (destroyed == True):
        return
    else:
        raccoon.go_right(2)
        search_and_destroy()


search_and_destroy()

raccoon.go_right()
raccoon.go_up(8)
        


    