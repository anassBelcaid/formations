"""
Créer une class tortue intélligente pour tracer
des formes complexes
"""

import turtle as T
import random
import math


#Créer une classe Smart Turtle qui se base sur la class Turtle

class SmartTurtle(T.Turtle):
    """
    Class intelligente qui peut tracer des formes complexes
    """
    def __init__(self, *args, **nargs):
        """
        passer les argument à la classe mère
        """

        super().__init__(*args, **nargs)


        #Choisir une couleur pour l'agent color(R, G, B)
        self.color(random.random(), random.random(), random.random())

        #Choisir la vitesse
        self.speed(-1)

        #choisir la taille du stylo
        self.pensize(2)

    
    def rectangle(self, L):
        """
        Fonction pour tracer un rectangle
        """

        for _ in range(4):
            self.forward(L)
            self.left(90)

    def polygon(self, L, n):
        """
        Affiche un polygone de longueur L contenant n faces
        """
        angle = 360 // n

        for _ in range(n):
            self.forward(L)
            self.left(angle)

    def ball(self, L, n):
        """
        Afficher une balle remplie d'arcs en couleurs
        """

        angle = 360/ n
        eps = 1/n

        #Couleur initial
        R = (1, 0, 0)  #R, G, B

        for i in range(n):

            #choisir la couleur
            self.color(1 - i*eps, 0, i*eps)

            #Tracer le premier arc
            self.circle(L, 180)
            #revenir à ma place
            self.circle(L, -180)

            #tourner par angle
            self.left(angle)


    def petal(self, L):
        """
        Fonction pour tracer une petale d'une fleure
        """


        self.speed(1)

        #Commencer le remplissage
        self.begin_fill()

        self.circle(L, extent = 90)
        self.left(90)
        self.circle(L, extent=90)


        #Terminer le remplissgae
        self.end_fill()


    def flower(self, L, n):
        """
        Fonction pour construire une fleur ayant n petals
        """

        for _ in range(n):

            #problème de répétition
            self.petal(L)






if __name__ == "__main__":
    
    t = SmartTurtle(shape='turtle')


    #Tracer une petale
    L = 100


    #Afficher un fleur ayant n petales
    t.flower(L, 8)


    #Afficher 4 fleurs




    T.exitonclick()
