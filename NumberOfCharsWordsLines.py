####### File Exercise from the book "Python For Everyone" by Horstmann #######
"""
p7.5 

    Write a program that asks the user for a file name 
    and prints the number of:
    characters, words, and lines in that file.
    
"""

file = open("input.txt", "w")
file.write("Mary had a little lamb\nWhose fleece was white as snow.\nAnd everywhere that Mary went,\nThe lamb was sure to go!")
file.close()

#I AM ASSUMING CHARACHTERS ONLY LETTERS
# TIME COMPLEXITY O(N)
def countCharacters(file):
    numberOfChars = 0
    char = file.read(1)
    while char != "":
        char = char.strip(".,?!")
        if char.isalpha():
            numberOfChars += 1
        char = file.read(1)
    return numberOfChars

# TIME COMPLEXITY O(N)
def countWords(file):
    numberOfWords = 0
    letter = file.read(1)
    word =""
    while letter != "":
        letter = letter.strip(".,?!")
        word += letter
        if not letter.isalpha():
            numberOfWords += 1
        letter = file.read(1)
    return numberOfWords

def countLines(file):
    countLines = 0
    for line in file:
        countLines += 1
    return countLines

def main():
    userInput = input("Enter file name: ")

    openFile = open(userInput, "r")
    print("Number Of Characters: ", countCharacters(openFile))
    openFile.close()

    openFile = open(userInput, "r")
    print("Number Of Words: ", countWords(openFile))
    openFile.close()

    openFile = open(userInput, "r")
    print("Number Of Lines: ", countLines(openFile))
    openFile.close()


main()
