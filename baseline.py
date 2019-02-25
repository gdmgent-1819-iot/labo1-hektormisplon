from sense_hat import SenseHat
import time
from random import randint
s = SenseHat()

# show string w/ bg color (method show_message)
# make color and bg color random, bg color should be darker
# loop

# string to show
message = "Hello! We are New Media Development"

# get random color - z index for background/foreground - defaults to foreground
def get_rand_color(z = 1):
    r, g, b = randint(0,255), randint(0,255), randint(0,255)
    if z == 1: 
      return (r, g, b)
    else:
      return (r/10, g/10, b/10)

# display the message
def loop_message():
    s.show_message(message, text_colour=get_rand_color(1), back_colour=get_rand_color(0))
    loop_message()
loop_message()
