from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = False

blue = (0, 0, 255)
white = (255,255,255)
nothing = (0,0,0)
delay = 0.2

def scotland():
    B = blue
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, W, B, B, B, B, W, O,
    O, B, W, B, B, W, B, O,
    O, B, B, W, W, B, B, O,
    O, B, B, W, W, B, B, O,
    O, B, W, B, B, W, B, O,
    O, W, B, B, B, B, W, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def scotland2():
    B = blue
    W = white
    O = nothing
    logo = [
    O, O, B, B, O, O, O, O,
    O, W, W, B, B, B, O, O,
    O, B, B, W, B, W, W, O,
    O, B, B, W, W, B, B, O,
    O, B, W, B, W, B, B, O,
    O, B, B, B, B, W, B, O,
    O, W, O, O, B, B, B, O,
    O, O, O, O, O, O, W, O,
    ]
    return logo
    
def scotland3():
    B = blue
    W = white
    O = nothing
    logo = [
    O, O, O, O, B, B, W, O,
    O, W, O, O, B, W, B, O,
    O, B, B, B, W, B, B, O,
    O, B, W, B, W, B, B, O,
    O, B, B, W, B, W, B, O,
    O, B, B, W, B, B, W, O,
    O, W, W, B, O, O, O, O,
    O, O, B, B, O, O, O, O,    
    ]
    return logo

while True:
  s.set_pixels(scotland())
  time.sleep(delay)
  s.set_pixels(scotland2())
  time.sleep(delay)
  s.set_pixels(scotland())
  time.sleep(delay)  
  s.set_pixels(scotland3())
  time.sleep(delay)    
