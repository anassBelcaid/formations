"""
Program to introduce the sys utilities

1- system version
2- system version info
3- recusion limit
4- arguments
4.1 Sum
4.2 Eval
"""

import sys



if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: first_program.py a op b")

    
    #getting the expression
    expr = " ".join(sys.argv[1:])
    print(eval(expr))
