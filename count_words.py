### A function which counts the number of words in a file



def count_words(filename):
    """Count the number of words in filename"""
    
### Opening and reading the file.txt and instantiating as a file_object
###using the try-except-else block to see if the file.txt is present
    try:
    
        with open(filename) as file_object:
            text_content = file_object.read()
    except FileNotFoundError:
        pass
        ### print("The file " + str(filename) + " is not present in this directory")

    else:
        ###Put each word in a list. split() does this
        words = text_content.split()

        ### Store in a variable and determine the length of the list = total words
        num_words = len(words)
        print("The number of words in the text file " +  str(filename) + " is = " )
        print(num_words)
