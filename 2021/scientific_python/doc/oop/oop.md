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


From a prototpye (class), we could create several **Objects** that share the
same structure but with **differents** values for each attributes. To illustrate
this concept, Let's consider a prototype for `Car` as depicted in the following
figure:

<center>
<img src="/assets/class_vs_objects.png" width="80%" height="200">      
</center>

From this class, we could create several **objects** by simply choosing a color
and manufacturer. In the figure, we see the creation of three of these objects.

> Hence an object is the instantiation of an class. Here the word instantiation
means to choose values for each attributs


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





So, we will start by declaring the prototype name which is `Robot`:

```python
class Robot():
  """
  Prototype for a Robot class
  """
```


### Constructor ###

The main method to tell the **python** interpreter how to construct a Robot is a
special method called the `Constructor` which, as its name indicates, serves to
construct (**instantiate**) a Robot.

```python

def __init__(self, Id, x, y):
  """
  Constructor for a robot with a given (id, x, y)
  """

  #Here we could choose how to create our object
  # from the given data (Id, x, y)
  self.Id = Id
  self.x = x
  self.y = y
```

Here we remark a curious argument called `self`. In the class methods, we will
be forced to use this argument to refer to the current object. 

> We could change the name of this variable but by convention we will always
name it self. 

> The argument self hase the same meaning of **this** in Java or C++


With just this declaration, we could now create simples **Robots**

```python
  #Create the first object R
  R1 = Robot('R', 3, 4)
  
  #Create a second object G
  R2 = Robot('G', 4, 8)
```
Suppose, we want to access the attributes of an object. We do this using the
**dot operator**.

```
Object.attribut
```


For example, suppose we want to print the position of the first robot:

```python
  print("Robot {}: at position ({},{})".format(R1.id, R1.x, R1.y))
```

## Methods ##
  <a name='methods'></a> 
Using this operator we could implement the rest of the methods.


```python
def getX(self):
  """
  return the x coordinate
  """
  return self.x

def getY(self):
  """
  return the y coordinates
  """
  return self.y

def move(self, x1, y1):
  """
  Move the to a new position (x1, x2)
  """

  self.x, self.y = x1, y1

def findPath(self, x1, y1): 
  "produce a list of directins[->,^,v, <] to get 
  the new position (x1,y1)
  Exercice
  """
  pass
```



### Exercise ###

1. Create a class `Student` with the following specifications:
  - An instance variable called `scores` to hold the student's **5** exam
  scores.
  - A constructor that read $$5$$ integers and stores them as the scores.
  - A method `calculateTotalScore` that return the sum of scores.

2. Create a program that read a set scores, and print the total score of each
   student.

## Encapsulation ##
  <a name='Encapsulation'></a> 

On the main advantages of the OOP paradigm is `Encapsulation`. It means that
internal representation is **hidden** from the user. We only expose the needed
methods. 


<center>
<img src="/assets/ensapsulation.png" width="40%" height="130">      
</center>


The main advantage of this approach is the gain in flexibility. We could change
the internal implementation without modifying  the external Application
Programming Interface (API). To illustrate this concept, let's consider our
class `Robot` and consider the simple program the manipulate a single robot in
grid of **positive numbers**

```python
R = Robot("R", 3, 4)

#move the object to (8,5)
R.x , R.y = 8, 5

#Move the object to (-1, 5),  not possible as our grid x>0 and y>0
R.x , R.y = -1, 5
```

With our current implementation of a Robot, the program will run without any
problem. 

> Already, we could sense the problem of exposing the internal implementation (x,
y), as the user could set those values to unknown values


<center>
<img src="/assets/polar_coordinates.PNG" width="30%" height="100">      
</center>

Suppose now, that our boss tell us that we should move to `polar coordinates`
instead of **Cartesian coordinates**. Which means that will represent the
position with $$(r,\theta)$$ instead of $$(x,y)$$. We could already see that the
program **will not run** as our objects don't have a $$x$$ and $$y$$ attributes
anymore


In order to make the jump, we will **encapsulates** the $$x,y$$ in the first
program, and create special methods (called *getter/setters*) in order to access
those attributes.

> By convention, a hidden attribute name in `Python` starts with _

```python
class Robot():
  """
  Class Robot with encapsulation
  """

  def __init__(self, x, y):
    """
    Create a Robot in the (x,y) coordinate
    """

    #by adding _ we declare that x is hidden(private)
    self._x, self._y = x, y

  #getter to give a controlled access to those methods
  def getX(self):
    return x

  def getY(self):
    return y

  def setX(self, x):
    """
    Apply control >0
    """
    self._x = x if x >= 0 else self._x

```


A program that uses this class, will look like this:

```python

R = Robot(3, 4)

#set position
R.setX(8)  

#Change y position will not work as y<0
R.setY(-1)

print("R position is ({},{})".format(R.getX(), R.getY()))

## Special methods ##
  <a name='specialMethods'></a> 

## Inheritance
  <a name='inheritance'></a> 

## Application
  <a name='Application'></a> 
