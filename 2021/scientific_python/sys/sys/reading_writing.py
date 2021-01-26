"""
Program to read and write data using the sys module

1. sys.stdin.readline()
2. sys.stdout.write
"""

import sys


if __name__ == "__main__":
    
    #Reading a value
    print("Donner une valeur:" )
    A = sys.stdin.readline()

    #Afficher avec stdout
    sys.stdout.write("A valeur")

