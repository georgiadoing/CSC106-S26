# Author: <Your name>
# Purpose: <Your description>

import turtle, random

def random_ratio_rectangle(x, y, size):
    """Draws a rectangle at location (x, y). The given size determines the
    width. The height is scaled with respect to the width. The scaling
    factor is randomly chosen to be a float between 0 and 2.
    """
    ratio = random.randrange(0,2) + random.random()
    rectangle(x, y, ratio*size, size)

def random_shape(x, y, size):
    """Picks and draws a random shape of size size at location (x,y)."""
    shape = random.choice([square, random_ratio_rectangle, circle, triangle])
    shape(x, y, size)

