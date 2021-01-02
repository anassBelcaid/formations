class Robot():

    """
    Simple base class
    """

    def __init__(self, x, y):

        self._x = x
        self._y = y

    def __str__(self):
        
        return "({:.2f}, {:.2f})".format(self._x, self._y)
    
    def __repr__(self):
        return self.__str__()
