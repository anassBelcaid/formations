"""
Script to illustrate the walking processus by 
"""
import os
from ipdb import set_trace



#changing the current directory

os.chdir("../../")



#Walking
start_path= os.getcwd()
for root, folders, files in os.walk(start_path):

    #Creating the root
    R = root.replace(start_path, "")

    level= R.count(os.sep)         # Count the number of separators
    indent = level * "    "


    for F in files:
        print("{}{}{}".format(indent,R, F))




