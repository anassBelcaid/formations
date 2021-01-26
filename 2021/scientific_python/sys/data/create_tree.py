"""
Create a tree in according to the town
"""
import os
import pandas as pd


def save_entry(root,name, date, town, salary,balance):
    """
    Save a client starting from root
    """

    #Creating the folder to save
    save_folder= root + "/" +  str(town)

    #Creating the folder
    os.makedirs(save_folder, exist_ok= True)


    #saving the file
    file_name = save_folder + "/"+ "clients.csv"

    if not os.path.exists(file_name):
        with open(file_name, "w") as F:
            F.write("name, date, town, salary, balance\n")

    with open(file_name, "a") as F:
     F.write("{}, {}, {}, {}, {}\n".format(name, date, town, salary,balance))



if __name__ == "__main__":
    
    #Reading the data
    data = pd.read_csv("./clients.csv")


    #Creating a directory
    root = "by_towns"

    
    #Loop over each entry and save it
    for i, entry in data.iterrows():
        save_entry(root,*entry)


