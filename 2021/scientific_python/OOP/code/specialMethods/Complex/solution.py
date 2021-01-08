import math


#Create a class Complex and overlaod its basic operators
class Complex(object):

    #Constructor
    def __init__(self, real, imaginary):
        #Add code here
        pass
        
    def __add__(self, no):
        #add code here
        pass
        
    def __sub__(self, no):
        #Add Code here
        pass

    def __mul__(self, no):
        #Add code here
        pass
        

    def __truediv__(self, no):
        #Add code here
        pass

    def mod(self):
        # Add code here
        pass
        

    def __str__(self):
        ## Str representatation given for you
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
