"""
Solution procedurale pour lire et trier les clients selon l'ordre alphabetique
"""



def lire_clients(emplacement):
    """
    Fonction pour lire le contenu des clients à partir de l'emplacment 
    spécifié.
    Un client sera spécifié comme une liste
    """


    with open(emplacement, "r") as F:

        # lire l'entete
        header = F.readline()
        print(header)





if __name__ == "__main__":
    lire_clients("/home/anass/teaching/formations/2021/scientific_python/OOP/code/why_oop/data/clients.csv")

    







