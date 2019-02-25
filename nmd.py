from sense_hat import SenseHat
import time
from random import randint
s = SenseHat()

# show letters from string w/ random color (method show_letter)
# 1 sec each, after last letter wait 2 seconds
# Uitbreiding: Maak de tekst (string) en de snelheid van de loop instelbaar via CLI.

# string to show
message = "NMD"

# random color
def get_rand_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

# function to display the message loop
def show_message():
    for i in message:
        s.show_letter(str(i), get_rand_color())
        time.sleep(1)
    s.clear()
    time.sleep(2)
    show_message()
show_message()
