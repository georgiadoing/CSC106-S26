###############################################################################
# Georgia Doing (doingg@union.edu)
#
# Turtle triangle with optional param
# In class demo
###############################################################################

import turtle

# example function with optional param
def turt_triangle(color = "black"):
    turtle.pencolor(color)
    for side in range(3):
        turtle.forward(75)
        turtle.left(120)


# set pensize so easier to see
turtle.pensize(5)

# draw a black triangle (default color)
turt_triangle()

# move so shapes don't overlap
turtle.teleport(100,100)

# draw a red triangle
turt_triangle("red")


