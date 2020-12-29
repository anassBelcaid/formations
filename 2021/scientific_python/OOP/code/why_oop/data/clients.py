import datetime
import pandas as pd
import numpy as np
from random import randint, choice

counter_name = 1
towns = ["Rabat", "Fes", "Meknes", "Tanger", "Casablanca"]


def generate_client():
    """
    generate a random client with the following information
    1. name
    2. date
    3. Town
    4. Salary
    5. balance
    """
    global counter_name

    name = "Client_" + str(counter_name)
    counter_name += 1

    #generate the date
    date = datetime.date(randint(2000, 2020), randint(1,12), randint(1,30))

    #country
    town  = choice(towns)

    #Salary
    salary = randint(1000, 5000)


    #balance
    balance = randint(0, 20000)


    return name, date, town, salary, balance




if __name__ == "__main__":
    

    num_client = 20
    clients = []

    for _ in range(20):
        clients.append(generate_client())
    clients= np.array(clients)
    np.random.shuffle(clients)

    columns = ['name','date', 'town', 'salary', 'balance']
    ds = pd.DataFrame(clients, columns=columns)
    ds.to_csv("clients.csv", index=False)














