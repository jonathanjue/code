#auto mine bot
import pydirectinput as p
import time
#back to game
p.click(1000,250)
time.sleep(1)

counter = 0

#mine top and bottom block

p.mouseDown()
time.sleep(1)
p.mouseUp()
p.moveRel(0,250)
p.mouseDown()
time.sleep(1)
p.mouseUp()
#move forward
p.press("w")
p.press("w")
p.press("w")
p.press("w")

#lookup
p.move(0,-250)

counter