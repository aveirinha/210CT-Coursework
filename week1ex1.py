def main():
    print("please insert a string")
    s1 = input()
    print("please insert other string")
    s2 = input()
    combineStr(s1, s2)

    


def combineStr(str1, str2):
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
