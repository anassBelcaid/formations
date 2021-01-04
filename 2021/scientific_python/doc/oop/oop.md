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
```

## Special methods ##
  <a name='specialMethods'></a> 


Another cool concept of **OOP** is the possibility to overload the [data Mode](https://docs.python.org/3/reference/datamodel.html) in order to simplify the syntax of our new created structure.

Let's reconsider the example of our vanilla *Robot* class. Imagine we want now,
to print its state to **file stream**. We could write a method such as:

```python
def print(self):
  """
  method to print the current Robot
  """
  print(f"Robot at ({self.getX()},{self.getY()})")
```

And inorder to use this method, we will call it as follow:

```python
R = Robot(3, 4)
R.print()
```

Imagine now that we are printing in a **file** instead of the standard output.
How, we will need *another* method in order to print the same content into the
new file.

> It will be much easier, if python could now how to convert our object into a
**string**, and then write its content using any useful methods such as:
  - print
  - write


Luckily, `Python` implements this data model and offer a set of useful hidden
methods that could be implicitly called by a given operator. For example in
order to convert an object into a **string**, python looks for the
implementation of a special methods called `__str__(self)`. Let's try is out:


```python
  def __str__(self):
    """
    method to convert the current object
    into a string
    """

    return "({:2.f}, {:.2f})".format(self.getX(), self.getY())
```

Now, we could use our object in function that accept string.

```python

R = Robot(1,3)

#will print (1.00, 3.00)
print(R)


#same into a file
with open("file.txt", "w") as F:
  #write the content of R into the file 
  F.write(R)
```

Here is a list of those useful functions

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-5nj1{border-color:inherit;font-family:"Lucida Console", Monaco, monospace !important;;text-align:left;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"><span style="font-weight:bold">Name</span></th>
    <th class="tg-0pky"><span style="font-weight:bold">Effect</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-5nj1">__init__</td>
    <td class="tg-0pky">Create an object</td>
  </tr>
  <tr>
    <td class="tg-0pky">__del__</td>
    <td class="tg-0pky">Called when an object is destroyed</td>
  </tr>
  <tr>
    <td class="tg-0pky">__repr__ </td>
    <td class="tg-0pky">Called to get an representation similar to str</td>
  </tr>
  <tr>
    <td class="tg-0lax">__str__</td>
    <td class="tg-0lax">String convertion of an object</td>
  </tr>
  <tr>
    <td class="tg-0lax">__lt__</td>
    <td class="tg-0lax">to compare two object <span style="font-weight:bold">x &lt; y</span></td>
  </tr>
  <tr>
    <td class="tg-0lax">__gt__</td>
    <td class="tg-0lax">to compare two objects <span style="font-weight:bold">x&gt;y</span></td>
  </tr>
  <tr>
    <td class="tg-0lax">__le__</td>
    <td class="tg-0lax">Compare two objects <span style="font-weight:bold">x&lt;= y</span></td>
  </tr>
  <tr>
    <td class="tg-0lax">__ge__</td>
    <td class="tg-0lax">Compare two objects <span style="font-weight:bold">x&gt;= y</span></td>
  </tr>
  <tr>
    <td class="tg-0lax">__eq__</td>
    <td class="tg-0lax">Compare two objects <span style="font-weight:bold">x== y</span></td>
  </tr>
  <tr>
    <td class="tg-0lax">__hash__</td>
    <td class="tg-0lax">Custom hash value for the object</td>
  </tr>
</tbody>
</table>


### Exercise ###

Our goal is to read a set of Box defined by their length $$l$$, breadth $$b$$
and height $$h$$. The goal is print those boxes in an ascending order of their
**volume**. So

1. Create a Custom class ``Box`` with three attributes $$(l, b, h)$$.
2. Implement the `computeVolume()` function.
3. Implement the `__str__` and `__repr__` to print a box like `Box[l, b, h],
   Vol=volume`
4. Overload the $$<$$ operator to compare those objects by **volume**.
5.Suppose now, that we want to keep only Boxes with different volumes.
   i.e. If two boxes share the same volume, we discard one of them.


## Inheritance
  <a name='inheritance'></a> 

[**Inheritance**](https://en.wikipedia.org/wiki/Inheritance) is the second major fundamental of **OOP**. It allows for fast
prototyping and code reuse. Generally, if we want to solve a given problem, most
probably, we could use **predefined objects** that are close to our solution. It
will be much easier to customize those objects to our need rather than creating
a full object from scratch. This enters in the well known concept of 

> Do not [Reinvent the wheel](https://en.wikipedia.org/wiki/Reinventing_the_wheel)


For example, Suppose now that we want to see our robot with cheerful **colors**.
It will be **cumbersome** to rewrite the class `Robot` from scratch. Especially,
if the new robots share the `same structure` but simply add a color attribute. 

Fortunately, We could create a new class by **inheriting** all the aspect of a
given class (called **base class**). In *Python*, we could use the following
syntax:


```python
class ColeredRobot(Robot):
  """
  Observe here that we specified a Robot in parentheses
  """
```

With this alone declaration, we didn't **add** anything to the existing class,
and we could use `ColoredRobot` as replacement for the `Robot` class. 

But we are interested in **extending** this class by adding a color attribute
defined in the [**RGB**](https://en.wikipedia.org/wiki/RGB_color_model). First
thing to do is define that in **constructor**.

```python
def __init__(self, x, y, R, G, B):
  """
  Constructor with all the fields
  """

  #Call for the base class constructor
  super().__init__(x,y)

  #Create the other fields
  self.R = R
  self.G = G
  self.B = B
```

Here we must pay careful attention to the line `super().__init__(x,y)`. It will
call for the **constructor** for the base class which is `Robot`.

If we print a **Colored Robot**, we will still have a simple printing of the
$$(x,y)$$ position but not the colored fields `(R, G, B)`. We need to change our
`__str__` function also to consider the additional fields.



```python

def __str__(self):
  """
  Define a string representation of our class
  """

  #first we get the representation of the base class
  R = super().__str__()

  #Now we add the color information
  return R + "[color]({},{},{})".format(self.R, self.G, self.B)
```
Here, also we remark the use of `super().__str__()` to call for the base class
representation. Otherwise we will write down the full implementation from
scratch.


### Exercise ###

You are given two classes, `Person` and `Student`, where **Person** is the base
class and **Student** is the derived class. You are given the complete code for
**Person** and the declaration for the **Student** class. Your task is to
complete the **Student** class by writing the following:

1. A Student class constructor, which has 4 parameter
  - A string *firstName*.
  - A string *LastName*
  - An integer *idNumber*
  - An list of integers to store the *scores*

2. A method `calculate` that return a `char` representing its mean according to
   the current scale:
<center>
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-2poh{border-color:inherit;font-family:"Palatino Linotype", "Book Antiqua", Palatino, serif !important;;text-align:center;
  vertical-align:top}
.tg .tg-hsiw{background-color:#fffe65;border-color:#333333;
  font-family:"Palatino Linotype", "Book Antiqua", Palatino, serif !important;;text-align:center;vertical-align:top}
.tg .tg-mpez{border-color:inherit;font-family:"Palatino Linotype", "Book Antiqua", Palatino, serif !important;;font-size:14px;
  text-align:center;vertical-align:top}
</style>
<table class="tg" style="undefined;table-layout: fixed; width: 261px">
<colgroup>
<col style="width: 95px">
<col style="width: 166px">
</colgroup>
<thead>
  <tr>
    <th class="tg-hsiw"><span style="font-weight:bold">Letter</span><br></th>
    <th class="tg-hsiw"><span style="font-weight:bold">Average</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-2poh">O</td>
    <td class="tg-2poh">90 &lt;= a &lt;= 100<br></td>
  </tr>
  <tr>
    <td class="tg-2poh">E</td>
    <td class="tg-2poh">80 &lt;= a &lt; 90<br></td>
  </tr>
  <tr>
    <td class="tg-2poh">A</td>
    <td class="tg-2poh">70 &lt;= a &lt; 80<br></td>
  </tr>
  <tr>
    <td class="tg-2poh">P</td>
    <td class="tg-2poh">55 &lt;= a &lt; 70<br></td>
  </tr>
  <tr>
    <td class="tg-2poh">D</td>
    <td class="tg-2poh">40 &lt;= a &lt; 55<br></td>
  </tr>
  <tr>
    <td class="tg-2poh">T</td>
    <td class="tg-2poh">a &lt; 40<br></td>
  </tr>
</tbody>
</table>

</center>



## Application
  <a name='Application'></a> 

[Turtle](https://docs.python.org/3/library/turtle.html) is graphical implementation of our **Robot**. It has already all the fields that we used and a bunch of additional useful fields.

Let's consider a simple example, where our Robot (now called a `turtle`) that
will move in a 4 directions to create a simple rectangle.


```python
"""
Simple script to draw a rectangle
"""

import turtle as T


if __name__ == "__main__":

    #Creating a simple turtle
    L = 200   # length of the rectangle


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
    T.exitonclick()
```


<center>
<img src="/assets/rectangle.png" width="150" height="150">      
</center>

Here is an explanation for the main components of this program:

- `t = T.Turtle(shap='turtle')` will create a Turtle with a specified shape.
- `t.pensize(2)`: will change the width of the drawing pen.
- `t.forward(L)`: Will advance the turtle by a lenght of $$L$$.
- `t.left(90)`: will turn the Turtle by 90 **degrees** left.


> For a list of useful function, check this brief [reference](https://perso.limsi.fr/pointal/_media/python:turtle:turtleref.pdf)

Our goal now, is to create a smart **Turtle** that could draw complex
**shapes**. We will use the concept of **inheritance** to get all the attributs
of the **Turtle** and we will add our own methods.

### SmartTurtle ###

- Create a class `SmartTurle` that inherite from the base class
**turtle.Turtle**.

- Add a constructor that pass all of its argument to the base constructor.
- Fix a random color for this turtle ( see module `random` for random number
generation)
-  Set the speed of the turtle as the max allowed speed.
-  Make the pen size as **2**.


### Drawing Rectangles ###

- Add a method called `rectangle( L)` that make the agent draw a rectangle
of lenght $$L$$.
- Using this method create the following figure:

<center>
<img src="/assets/rectangle_serie.png" width="150" height="150">      
</center>

### Drawing polygons ###

- Create a method called `polygon(L, n)`  that create a polygon of lenght $$L$$
with $$n$$ faces. (For example the `polygon(L,3)` will create a **Triangle** and `polygon(L,4)` will creae a square).

- Use this function to repreduce the following figure:

<center>
<img src="/assets/polygones.png" width="150" height="150">      
</center>


### Circles ###

The function `circle` could be used to draw circles. It has the following
syntax:

```python
  t.circle(radius, extent, steps)
```

where:

- radius : The radius of the circle.
- extent  : The angle of the Drawn arc.
- steps   : Number of points to use.


- Create a method for your inherited class called `coloredBall(R)` to draw a
colored ball with radius $$R$$ as shown in the figure:


<center>
<img src="/assets/colored_ball.png" width="200" height="200">      
</center>

Now, we could use the method **circle** to create a simple flower.

- Add a method `petal(L)` to create a flower petal as shown in the figure. Thik
to combine two arcs with extent $$\dfrac{\pi}{4}$$:


<center>
<img src="/assets/petal.png" width="200" height="200">      
</center>


- Using this function, make the Turtle draw a `flower` by specifying its lenght
and number of petals. The figure shows those flowers with differents number of
petals.

<center>
<img src="/assets/flowers.png" width="80%" height="200">      
</center>


## Sierpinsky Triangle ##

Now, we will combine inheritance and **recurence** to create the classical [**Sierpinsky Triangle**](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle) show in the figure:



<center>
<img src="/assets/sierpensky.png" width="90%" height="150">      
</center>

1. In order to start write a simple function `Sierpensky(N)` that draws a filled
triangle of length $$L$$ (figure left).
2. From the figure, extract a **recursive** relation between a triangle and the
   one on its **left**.
3. Now modify the `Sierpensky(L, order)` to take an additional order with
   represent the order of decomposition in the triangle.

4. Change your program to produce the content of the figure.

### H Fractal ###
your challenge now (if you accept it), is to use the power of recurrence and
your knowledge on the Turtle world to produce the following **H fractal**.



<center>
<img src="/assets/H_fractal.png" width="90%" height="150">      
</center>
