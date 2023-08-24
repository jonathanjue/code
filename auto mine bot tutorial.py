#auto mine bot
import pydirectinput as p
import time





def mineblock():
    p.mouseDown()
    print("mining")
    time.sleep(mining_time)
    p.mouseUp()


def walkforward():
    print("walking")
    p.keyDown('shift')
    p.keyDown('w')
    time.sleep(1)
    p.keyUp('w')
    #time.sleep(0.1)
    p.keyUp('shift')
    #time.sleep(0.1)

#program begin
#counter
counter=0
mining_time = 1
look_amount = 300
#resume game
p.click(1000,250)
time.sleep(1)

while counter < 50:
    mineblock()
    p.moveRel(0,look_amount)
    mineblock()
    p.moveRel(0,-look_amount)
    walkforward()
    counter += 1

print("done")