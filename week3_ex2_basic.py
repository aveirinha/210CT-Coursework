#Time complexity: O(n)

def linearSearch(num_list, target):
    """This function receives a list of integer and 
    the value it needs to find. It is called recursively
    until gets to the target value or to the endo of the list.
    If the value is found it returns true if not it returns false"""
    if (len(num_list)>= 1):
        if (num_list[0] == target): #value was found
            print('Found')
            return True

        elif  (len(num_list) == 1): #reached the end of the list
            print('Not Found')
            return False 

        else:   #method calls itself again starting on the second element
            num_list.pop(0) 

            return(linearSearch(num_list, target))




def main():
    l = [3,5,7,1,2,9]
    t = 9

    linearSearch(l, t)


if __name__ == "__main__":
    main()
