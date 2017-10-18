import math

def main():
    print("Please insert a number")
    number = str(input())
    isArmstrong(number)


def isArmstrong(nr):
    nr_aux = list(map(int,str(nr)))
    
    if (int(nr_aux[0])**3 + int(nr_aux[1])**3 + int(nr_aux[2])**3 == int(nr)):
        print("Yes")
    else:
        print("No")


if __name__== "__main__":
  main()
