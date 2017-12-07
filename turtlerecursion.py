from turtle import *

# Recursive turtle graphics
def square(size):
    if size > 5:
        for i in range(0,4):
            forward(size)
            right(90)
        right(45)
        square(size-5)

square(100)

