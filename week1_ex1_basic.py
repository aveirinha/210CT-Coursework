"""This program recieves two strings from the user
and combines them in the method combineStr and then prints it"""

def main():
    """The following two while loops are responsible for
    checking that the input is valid for this program"""
    while True:
        try:
            s1 = str(input("please insert a string"))

        except ValueError:
            print("Sorry, that is not a string")

        if(type(s1) == str):
            break

    while True:
        try:
            s2 = str(input("please insert a string"))

        except ValueError:
            print("Sorry, that is not a string")

        if(type(s2) == str):
            break
    
    strfinal = combineStr(s1, s2)


def combineStr(str1, str2):
    """This method recives two strings,combines them
    prints the combination and returns it.
    It splits the strings into lists, creates a new one using a letter
    from str1 and str2 and covert the final list into a string again"""
    str1.split()
    str2.split()
    str3 = []
    if (len(str1) < len(str2)):
        val = len(str2)
    else:
        val = len(str1)
    for i in range(0, val):
        if( i <= (len(str1)-1) and i <= (len(str2) - 1)):
            str3.append(str1[i])
            str3.append(str2[i])
        elif( i <= (len(str1)-1)):
            str3.append(str1[i])
        else:
            str3.append(str2[i])
            
    strfinal = ''.join(str3)
    print(strfinal)
    
if __name__== "__main__":
  main()