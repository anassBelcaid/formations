class Box():
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __hash__(self):
        return hash(self._x * self._y)
    
    def __eq__(self, other):
        return self._x * self._y == other._x * other._y

    def __str__(self):
        return f"({self._x}, {self._y})"

    def __repr__(self):
        return self.__str__()



if __name__ == "__main__":
    
    B1 = Box(4,3)
    B2 = Box(2,4)
    B3 = Box(2,6)

    Boxes = [B1, B2, B3]


    B_set = set(Boxes)
    print(*B_set, sep="\n")


