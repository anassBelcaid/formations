---
layout: page
date: 2021/01/09
permalik: /oop/oop/
---



## Table de matière ##

- [Why OOP](#WhyOOP)
- [Classes](#Classes)
- [Encapsulation](#Encapsulation)
- [Methods](#methods)
- [Special methods]( #specialMethods )
- [Inheritance](#inheritance)
- [Application](#Application )

## Why OOP ##
<a name="WhyOOP"> </a>

<img src="/assets/oop_why_oop_problem.png" width="90%" height="200">      

An entry of a client has the following form:



| Name   | Date   | Town | Salary | Balance| 
|--------|--------|------|--------|--------|
|        |        |      |        |        |

## Procedural solution ##

> A procedural solution concentrates on **actions** (verbs) and implements
those actions


<img src="/assets/oop_why_oop_procedural.png" width="90%" height="200">      

```python

"""
Solution procedurale pour lire et trier les clients selon l'ordre alphabetique
"""
def lire_clients(emplacement):
    """
    Fonction pour lire le contenu des clients à partir de l'emplacment 
    spécifié.
    Un client sera spécifié comme une liste
    """

    #initial list
    clients = [] 

    with open(emplacement, "r") as F:

        # lire l'entete
        header = F.readline()

        for line in F:
            name, date, town, salary, balance = line.split(",")

            #convertir les champs entiers
            date, salary, balance = map(int, [date, salary, balance])

            clients.append([name, date,town, salary, balance])

    return clients

def insert_sort(Clients, client):
    """
    Insérer le nouveau [client] dans le tableau [Clients]
    """

    #positin d'insertion
    pos = 0

    #comparaison par nom
    while pos < len(Clients) and  client[0] > Clients[pos][0]:
        pos += 1

    #Inserer dans la position pos
    Clients.insert(pos, client)


def trier_clients(Clients):
    """
    Trier les clients stockés dans une liste par leur nom.
    Le tri utilisé est un tri par insertion
    """

    #tableau initial contenant le premier client
    client_tries = [Clients[0]]


    #parcour du reste est insertion
    for client in Clients[1:]:
        insert_sort(client_tries, client)

    return client_tries


if __name__ == "__main__":
    clients = lire_clients("../data/clients.csv")

    print(*clients, sep="\n")

    trie = trier_clients(clients)
    print(80*'-', *trie, sep="\n")
```

We could observe several problems with this implementation:

- Poor **representation** ( A client **is not** a List)
- **Exposed** implementation: If we want to share this code, we also share it
implementation (how it was done). 
- **Reuse**:  This code is is not very handy in other situations. For example
the `read_clients` is only useful if we want to read **all** the clients, not
just for a single clients. Also we wrote a *two* functions to sort but they are
only useful if we apply the sort to **Clients**. But the sorting itself could be
used in a large set of situations.

## Approach OOP ##


> An OOP approach tries codes the **actors**(nouns) of a problem into useful
entities.


<img src="/assets/oop_why_oop_oop.png" width="90%" height="200">      

```python
"""
OOP solution to the problem of sorting clients
"""
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

if __name__ == "__main__":
    
    #Array of clients
    Clients = []

    with open("../data/clients.csv") as F:
        #skip header
        F.readline()
        
        for line in F:
            Clients.append(Client(*line.split(",")))

    #Sorting the array
    Clients.sort()
    print("{}{}{}{}{}".format("name".center(20), "town".center(20),
        "date".center(4), "salary".rjust(10,' '), "balance".rjust(10,' ')))

    print(*Clients, sep='\n')


```

### Advantages ###

- **Modular code**: The code is modular, meaning it is decomposed on several
useful **blocks**. For our case, we gain a unique block which is the `Client`.

- Reuse: Encourages the reuse of code.
- Flexibility: As seen in the demonstration, we changed the **key** for the
sorting algorithm by simply redefining the `__lt__` function.

## Classes 
<a name='Classes'></a>


> A class in **Python** is just a **container** that could store **data** or
**methods**.

<center>
<img src="/assets/classes_class_python.png" width="50%" height="150">      
</center>

> There is no prior limitation on those data nor methods. i.e, A class could
**evolve** while executing a program!!!


```python
"""
Simple class for a robot
"""
#Définir le robot
class Robot():
    """
    Simple class for a robot to move in a grid
    """

if __name__ == "__main__":

    #Créer un simple robot
    R1 = Robot()
    R1.x = 3
    R1.y = 4


    R2 = Robot()
    print(f"Robot at position: ({R1.x},{R1.y})")

    print(f"Robot at position: ({R2.x},{R2.y})")
```


We remark a big **drawback** here as both R1 and R2 are robots. But, they don't
**share** the same contents. That will problematic for someone who write a
program that manipulate those robots.




## Classes in general ##

In the general setting, a **class** is simply a prototype for a given data type. It specify the set of shared
**attributes** and a set of common useful functions called **methods**.

<center>
<img src="/assets/classes_class.png" width="30%" height="120">      
</center>


Let's try to apply this concept on our little example. We want to create
**Robot** that know his position and that could easily **move** in his grid
world.

1. First, let's try to think, how to **represent** a Robot. We could add any
   characteristic of a **Robot** such as (*model, engine, material....*). But
   for our need, we only want to know his **position** and **identity** as we
   could have multiple robot in the same grid world. Hence, we will characterize
   our robot with those three **attributs**:  
   - **X**: X position in the grid.
   - **Y**: Y Position in the grid
   * **Id**: Its id

2. Second, we need to add a set of functions (called **methods** in the OOP
   vocabulary) that facilitate the use of this
   Robot. Here the more the **merrier**. We could choose the following methods:
   - `getX`: A Robot must be aware of its position
   - `getY`: A Robot must be aware of its position
   * `getId`: A Robot must know his ID.
   * `Move`: Can easily change it position in the grid
   * `GetPath`: More useful, if could compute how he could move to any position
   $$(x,y)$$ in the world.


With such as decision the **UML diagram** for this class would be as follow:

<center>
<img src="/assets/classes_class_robot.png" width="35%" height="180">      
</center>






## Encapsulation
  <a name='Encapsulation'></a> 


## Methods ##
  <a name='methods'></a> 

## Special methods ##
  <a name='specialMethods'></a> 

## Inheritance
  <a name='inheritance'></a> 

## Application
  <a name='Application'></a> 
