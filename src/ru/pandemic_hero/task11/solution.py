import player
 
player.put_on_mask()
player.go_down()
player.go_left()
player.go_down()
 
virus_down = player.look(0, 1)
while (virus_down != 2):
    virus_down = player.look(0, 1)
player.disinfect(5)
player.go_down()
 
player.go_left()
 
virus_up = player.look(-1, -1)
while virus_up != 2:
    virus_up = player.look(-1, -1)

player.disinfect(6)
player.go_left(3)
player.go_up(2)
 
virus_down = player.look(-1, -1)
while virus_down != 2:
    virus_down = player.look(-1, -1)
 
player.disinfect(6)
player.go_left()
player.go_up()
player.wash_hands()