"""
Solution procedurale pour lire et trier les clients selon l'ordre alphabetique
"""
import datetime



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

    







