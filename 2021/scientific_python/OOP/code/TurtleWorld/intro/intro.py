"""
Simple script to draw a rectangle
"""

import turtle as T


if __name__ == "__main__":

    #Creating a simple turtle
    L = 200   # lenght of the rectangel


    #Create a turtle
    t = T.Turtle(shape='turtle')

    #Change the property of the pen
    t.pensize(2)

    #Draw four lines
    for _ in range(4):
        t.forward(L)

        #change angle by 90 degress
        t.left(90)
        



    #Exit the sceen on click
    # T.Screen().getcanvas().postscript(file="rectangle.eps")
    T.exitonclick()

