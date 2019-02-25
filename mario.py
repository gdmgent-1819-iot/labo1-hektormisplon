from sense_hat import SenseHat
import time
s = SenseHat()

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)

def get_mario(yPos):
    W = white
    O = nothing
    B = blue
    R = red
    mario_down = [
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, R, O, O, O,
    O, O, O, O, B, O, O, O,
    W, W, W, W, W, W, W, W,
    ]
    mario_mid = [
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O,
    O, O, O, O, R, O, O, O,
    O, O, O, O, B, O, O, O,
    O, O, O, O, O, O, O, O,
    W, W, W, W, W, W, W, W,
    ]
    mario_up = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, R, O, O, O,
    O, O, O, O, B, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    W, W, W, W, W, W, W, W,
    ]
    if yPos == 0:
      return mario_down
    elif yPos == 1:
      return mario_mid
    elif yPos == 2:
      return mario_up
      
def make_jump():
    s.set_pixels(get_mario(0))
    time.sleep(.05)
    s.set_pixels(get_mario(1))
    time.sleep(.05)
    s.set_pixels(get_mario(2))
    time.sleep(.2)
    s.set_pixels(get_mario(1))
    time.sleep(.05)
    s.set_pixels(get_mario(0))
      
while True:
    e = s.stick.wait_for_event()
    if e.action == "pressed" and e.direction == "up":
      make_jump()