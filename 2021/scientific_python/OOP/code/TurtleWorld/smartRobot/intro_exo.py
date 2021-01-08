"""
Using the simple interface, create four rectangles
"""


import turtle as T
from random import random
import math
pi = math.pi
from time import sleep


class SmartAgent(T.Turtle):

    """Smart Tutrtle with additional methods"""

    #{{{ Constructor
    def __init__(self, *args, **aargs):
        """Create a Smart Agent using the same argument for turtle.

        :*args: TODO

        """
        super().__init__(*args, **aargs)

        #Choose a random color
        self.color(random(), random(), random())

        #choose a speed
        self.speed(-1)


        #Set pen size
        self.pensize(2)
    #}}}
    #{{{Rectangle
    def rectangle(self, lenght):
        """
        Draw a rectangle of lenght L
        """
        for _ in range(4):
            self.forward(lenght)
            self.left(90)
    #}}}
    #{{{ polygon
    def polygon(self, L, n, fill=True):
        """
        Draw a polygon with n faces with lenght L
        """

        self.radians()
        if fill:
            self.begin_fill()

        angle = 2*math.pi / n

        for _ in range(n):
            self.forward(L)
            self.left(angle)

        if fill:
            self.end_fill()
        self.degrees()
    #}}}
    # Move into a position without drawing {{{ #
    def moveTo(self, x, y):
        """
        Move the agent into the position(x, y)
        without drawing
        """

        self.penup()
        self.setpos(x,y)
        self.pendown()
    # }}} Move into a position without drawing #
    # draw triangle {{{ #
    def triangle(self, P1, P2, P3, fill=True):
        """
        Draw a triangle P1, P2, P3
        """

        if fill:
            self.begin_fill()

            self.moveTo(*P1)
            self.setpos(*P2)
            self.setpos(*P2)
            self.setpos(*P3)
        if fill:
            self.end_fill()
    # }}} draw triangle #
    #{{{ Sierpensky
    def sierpensky(self, L, order=0):
        """
        Draw the sierpensky triangle of order:1
        """

        if order == 0:
            self.polygon(L, 3)

        else:
            angle = 360//3
            self.sierpensky(L//2, order -1)
            self.forward(L//2)
            self.sierpensky(L//2, order-1)
            self.left(angle)
            self.forward(L//2)
            self.right(angle)
            self.sierpensky(L//2, order-1)
            self.right(angle)
            self.forward(L//2)
            self.left(360//3)

#}}}
#{{{ Petal
    def petal(self, L):
        """
        Draw a petal
        """

        self.radians()
        self.begin_fill()
        self.circle(L, pi/4)
        self.left(pi-pi/4)
        self.circle(L, pi/4)
        self.left(pi-pi/4)
        self.end_fill()
        self.degrees()
        #}}}
#{{{ Flower
    def flower(self, L,N):
        """
        Create a flower with N petal
        """

        angle = (360)/N

        for _ in range(N):
            self.petal(L)
            self.left(angle)
            #}}}

    def H_fractal(self, L, order=0):
        """
        Draw the H fractal
        """
        if order < 0:
            return

        self.left(90)

        self.backward(L//2)
        self.left(90)
        self.backward(L//2)

        #firt derivation
        self.H_fractal(L//2, order-1)
        self.forward(L)

        #second derivation
        self.H_fractal(L//2, order-1)

        self.backward(L//2)
        self.right(90)
        self.forward(L)


        self.left(90)
        self.backward(L//2)

        #third derivation
        self.H_fractal(L//2, order-1)


        self.forward(L)

        #fourth derivation
        self.H_fractal(L//2, order-1)

        self.backward(L//2)
        self.right(90)
        self.backward(L//2)


        self.right(90)



if __name__ == "__main__":
    
    
    # Initial lenght
    L = 128

    t = SmartAgent(shape='turtle')
    t.pensize(2)
    # t.hideturtle()
    t.color('black')
    t.moveTo(-3*L,0)


    for order in [0, 1, 2, 3]:
        t.H_fractal(L,order)
        t.penup()
        t.forward(2*L)
        t.pendown()





    T.exitonclick()
