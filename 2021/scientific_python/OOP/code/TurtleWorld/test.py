import turtle as T


if __name__ == "__main__":
    
    # Longueur
    L = 200

    #Créer mon agent qui est un Tortue
    t = T.Turtle(shape='turtle')


    #Choisir la taille du stylo
    t.pensize(2)


    #Régler la vitesse
    t.speed(1)


    for _ in range(4):
        t.forward(L)
        t.left(90)






    #Empecher la fenetre de disparaitre
    T.exitonclick()
