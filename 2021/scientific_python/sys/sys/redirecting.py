"""
Simple program to illustrate redirecting system in
"""


import sys


#redirecting
sys.stdin = open("./input2.txt", "r")

if __name__ == "__main__":
    
    #Simple program to evaluate an expression
    a  = input()

    #Reading the operation
    op = input()

    #Reading the right hand side
    b = input()

    print(eval(" ".join(([a, op, b]))))
