from sense_hat import SenseHat
import time
from random import randint
s = SenseHat()

# loop through all leds w/ random color
# apply easing funciton
# extra: add easing via cli
s.clear()

def ease_in_out(amount):
  return amount

def loop_matrix():
  for i in range(8):
      for j in range(8):
          s.set_pixel(i,j, (randint(255), randint(255), randint(255)))
          time.sleep(ease_in_out(.5))
  s.clear()
  loop_matrix()
loop_matrix()