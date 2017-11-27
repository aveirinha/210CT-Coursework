"""This program recieves a three character integer from the user
and checks if it is an armstrong number"""

import math

def main():
    
    number = str(input("Please insert a number"))
    isArmstrong(number)


def isArmstrong(nr):
    """This method recieves a 3 digit """
    nr_aux = list(map(int,str(nr)))
    
    if (int(nr_aux[0])**3 + int(nr_aux[1])**3 + int(nr_aux[2])**3 == int(nr)):
        print("Yes")
    else:
        print("No")


if __name__== "__main__":
  main()
