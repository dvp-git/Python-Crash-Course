### Alice in wonderland , counting the entire words in the text file alice in wonderland

file_name = "alice in wonderland.txt"


### Opening and reading the file.txt and instantiating as a file_object


###using the try-except-else block to see if the file.txt is present
try:
    
    with open(file_name) as file_object:
        text_content = file_object.read()
except FileNotFoundError:
    print("The file is not present in this directory")

else:
    words = text_content.split()
    num_words = len(words)
    print("The number of words in the text file alice in wonderland is = " )
    print(num_words)
