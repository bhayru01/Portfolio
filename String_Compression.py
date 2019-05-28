"""
String Compression
Problem

Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. 
For this problem, you can falsely "compress" strings of single or double letters. 
For instance, it is okay for 'AAB' to return 'A2B1' even though 
this technically takes more space.

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.

"""
string = "AAAABBBBCCCCCDDEEEE"

##THIS FUNCTION COMPRESSES STRING WITH ONLY LETTERS, TO LETTER AND NUMBER OF OCCURRENCES E.G 'AAABBB' TO 'A3B3'
# @param string to compress
# @return compressed string
#
# TIME COMPLEXITY O(N), SPACE COMPLECITY O(N)
#
def compress(string):

    dictionary = dict() #ASSIGNING NEW DICTIONARY TO ADD THE ELEMENTS
    compressedString = "" #ASSIGNING NEW STRING TO PUT THE COMPRESSED ELEMENTS

    for element in string: #FOR EACH ELEMENT IN string
        if element in dictionary: #IF ELEMENT ALREADY IN DICTIONARY INCREASE THE CURRENT KEY'S VALUE WITH ONE
            dictionary[element] +=1
        else:
            dictionary[element] = 1 #ELSE ASSIGN KEY'S VALUE TO 1

    for key in dictionary: #FOR EACH KEY IN dictionary
        compressedString += key #ADD KEY
        compressedString += str(dictionary[key]) #ADD KEY'S VALUE

    return compressedString

#TEST CASES
test1 = '' #EXPECTED ''
test2 = 'AABBCC' #EXPECTED 'A2B2C2'
test3 = 'AAABCCDDDDD' #EXPECTED 'A3B1C2D5'
test4 = 'AAAaaa' #EXPECTED 'A3a3'


print(compress(test1))
print(compress(test2))
print(compress(test3))
print(compress(test4))
