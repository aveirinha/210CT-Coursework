#Time Complexity: O(n)
import string

def mirrorWords( word_list, word_list_rev):
    """This function recieves a list of words
    and prints every word on the list in 
    reversed order and returns them in a new  """
    if len(word_list) == 0:
        words_rev = ' '.join(word_list_rev)
        print(words_rev) #puts all the elements of the list in a string
        return words_rev

    else:
        word = word_list[0] 
        print(word[::-1])
        word_list_rev.append(word[::-1])
        word_list.pop(0)    #removes the first word so that when the funtion is called it starts with the second element

        return(mirrorWords(word_list, word_list_rev))



def main():
    
    words = input('Please insert a string: ')
    word_list = words.split() #creates a list with all the words in the string
    
    mirrorWords(word_list, [])


if __name__ == "__main__" :
    main()
