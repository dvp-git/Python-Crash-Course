### Wokring with multiple files to count words:

from count_words import count_words

filenames = ["WilliamShakespear.txt","CharlesDickens.txt","pass.txt","alice in wonderland.txt"]

### Using a for loop to count the words in each text file:

for filename in filenames:
    count_words(filename)


