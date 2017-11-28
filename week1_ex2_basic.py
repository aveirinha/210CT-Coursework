"""This program recieves a three digit integer from the user
and checks if it is an armstrong number"""

import math

def main():
    #This while loop assures the user input is
    #a 3 digit number
    while(True):
        number = str(input("Please insert a 3 digit number> "))
        if(len(number) == 3):
            break
    
    isArmstrong(number)


def isArmstrong(nr):
    """This method recieves a 3 digit integer and
    checks if it is an armstrong number"""
    nr_aux = list(map(int,str(nr)))
    
    if (int(nr_aux[0])**3 + int(nr_aux[1])**3 + int(nr_aux[2])**3 == int(nr)):
        print("Yes")
        return 'Yes'
    else:
        print("No")
        return 'No'


if __name__== "__main__":
  main()
