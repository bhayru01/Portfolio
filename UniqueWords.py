"""
Problem Statement. Determine the number of unique words contained in a text document.

"""
##The function creates a file with build in text
# @param filename, name for the file
#
def createFileWithDefaultText(filename):
        with open(filename, 'w') as file:
            file.write("Beray Nedim Hayrulah\nBehcet Nedim Hayrulah\nSelime Halibryam Halibryam\nNedim Behcet Halibryam")



## The function gets a character from a file to create a word and
## prints distinct total number of words
# @param file, file to get the characters from
#
def uniqueNumberOfText(file):
    #Single char from a file
    letter = file.read(1)
    word = ""
    setOfWords = set()
    #while it is not the end of file
    while letter != "":
        #removing special characters from the character
        letter = letter.strip(".,?!")
        # if not the end of word and not newline
        if letter != " " and letter != "\n":
            word += letter
        else :
            setOfWords.add(word)
            word = ""
        #single char from the file
        letter = file.read(1)
    #adding the last word from the file
    setOfWords.add(word)
    print(setOfWords)
    #the len of the set is the unique total word number from a file
    uniqueNumber = len(setOfWords)
    print(uniqueNumber)

def main():
    filename = input("Enter filename: ")

    createFileWithDefaultText(filename)

    with open(filename, 'r') as file:
        print("Number of unique words contained in a text document: ", end="")
        uniqueNumberOfText(file)
