"""
OOP solution to the problem of sorting clients
"""

#{{{ Class client
class Client():
    """
    Definition de la classe Client
    """

    def __init__(self, name, date, town, salary, balance):
        """
        Constructor using the field
        """
        self.name = name
        self.town = town
        self.date = int(date)
        self.salary = int(salary)
        self.balance = int(balance)

    def __lt__(self, other):
        """
        Show to python how to compare two objects
        """

        return self.name < other.name
    
    def __str__(self):
        """
        Show to python how to print a client
        """

        return "{}{}{:4d}{:10d}{:10d}".format(self.name.center(20),
                self.town.center(20), self.date, self.salary, self.balance)

    def __repr__(self):
        return self.__str__()
#}}}


if __name__ == "__main__":
    
    #Array of clients
    Clients = []

    #{{{ Loading the data
    with open("../data/clients.csv") as F:
        #skip header
        F.readline()
        
        for line in F:
            Clients.append(Client(*line.split(",")))
    #}}}
    #{{{Sorting the clients
    Clients.sort()
    #}}}
    #{{{ Printin the results
    print("{}{}{}{}{}".format("name".center(20), "town".center(20),
        "date".center(4), "salary".rjust(10,' '), "balance".rjust(10,' ')))

    print(*Clients, sep='\n')
    #}}}


