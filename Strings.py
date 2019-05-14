"""
Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
"""

#string = "google.com"

def numberOfChars(string):
    charNumbers = ""
    for i in range(len(string)):
        letter = string[i]
        counter = 0
        for j in range(len(string)):
            if string[j] == letter:
                counter += 1
        if letter not in charNumbers:
            charNumbers = charNumbers + "'" + letter + "'" + ": " + str(counter) + ", "
    return charNumbers

#############################################################################################



"""
Write a Python program to get a string made of the first 2 and the last 2 chars
from a given a string.
If the string length is less than 2, return instead of the empty string.
 
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
"""

#string = "w3resource"

def firstAndLast(string):
    if len(string)<2:
        return ""
    else:
        firstTwo = string[0:2]
        lastTwo = string[-2:]

        modifiedString = firstTwo + lastTwo
        return modifiedString

#print(firstAndLast(string))


#############################################################################################

"""
Write a Python program to get a string from a given string, 
where all occurrences of its first char have been changed to '$',
except the first char itself.

Sample String : 'restart'
Expected Result : 'resta$t'

"""

#string = 'restart'

def changeLetter(string):
    firstLetter = string[0]
    newString = firstLetter
    dolarSign = "$"
    for i in range(1, len(string)):
        if firstLetter == string[i]:
            newString += dolarSign
        else:
            newString += string[i]
    return newString

#print(changeLetter(string))


#############################################################################################


"""
Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.

Sample String : 'abc', 'xyz' 
Expected Result : 'xyc abz'

"""

#stringA = "abc"
#stringB = "xyz"

def swapStrings(stringA, stringB):
    swappedString = stringB[0:2] + stringA[-1] + " " + stringA[0:2] + stringB[-1]
    return swappedString

#print(swapStrings(stringA, stringB))



#############################################################################################

"""

Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead.
If the string length of the given string is less than 3, leave it unchanged.
 
Sample String : 'abc'
Expected Result : 'abcing' 
Sample String : 'string'
Expected Result : 'stringly'

"""

#testString = input("Add string: ")

def addToEnd (string):
    addIng = 'ing'
    addLy = 'ly'
    newString = ""
    if len(string) >= 3:
        if addIng == string[-3:]:
            newString = string + addLy
        else:
            newString = string + addIng
    else:
        newString = string

    return newString

#print(addToEnd(testString))


#############################################################################################


"""
7. Write a Python program to find the first appearance of the substring 'not' and 'poor'
from a given string, if 'not' follows the 'poor',
replace the whole 'not'...'poor' substring with 'good'.
Return the resulting string.

Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'

"""

#testString = 'The lyrics is not that poor!'

def changeString(string):
    notPosition = string.find('not')
    poorPosition = string.find('poor')
    newString = ""

    if notPosition > 0:
        if poorPosition > notPosition:
            newString = string[0:notPosition] + "good" + string[poorPosition+4: ]
    else:
        newString = string
    return  newString

#print(changeString(testString))



#############################################################################################



"""
8. Write a Python function that takes a list of words
    and returns the length of the longest one
"""
## I didnt use any data structures like lists, tuples or dictionaries!!!##



#testString = "Beray Nedim Hayrulah Bekobekobeko"

def longestWord(string):
    counter = 0
    previousCount = 0

    for i in range(len(string)):
        if string[i] == " " or i == len(string)-1:
            if counter >= previousCount:
                if i == len(string)-1:
                    counter += 1
                previousCount = counter
                counter = 0
        else:
            counter += 1

    return previousCount

#print(longestWord(testString))


#############################################################################################

"""
9. Write a Python program to remove the nth index character from a nonempty string
"""

#testString = "Hayrulah"

def removeIndex(index, string):
    firstPart = string[:index]
    secondPart = string[index+1:]
    removedLetter = firstPart + secondPart
    return removedLetter

#print(removeIndex(4, testString))

#############################################################################################

"""

10. Write a Python program to change a given string to a new string 
    where the first and last chars have been exchanged.
"""

#testString = "Beray"

def swapFirstAndLast(string):
    newString = string[-1]+string[1:-1]+string[0]
    return newString

#print(swapFirstAndLast(testString))


#############################################################################################

"""
11. Write a Python program to remove the characters
    which have odd index values of a given string.
"""
#testString = "Hayrulah"

def removeOddString(string):
    newString = ""
    for i in range(len(string)):
        if i % 2 == 0:
            newString += string[i]

    return newString

#print(removeOddString(testString))


#############################################################################################


"""
12. Write a Python program to count the occurrences of each word in a given sentence
"""

#testString = "I am King of the world"

def countWords(string):
    counter = 0
    for i in range(len(string)):
        #if the char is the last character
        if string[i] == string[-1]:
            counter += 1
        #if the character is not string
        if not string[i].isalpha():
            counter += 1

    return counter

#print(countWords(testString))

#############################################################################################

"""

13. Write a Python script that takes input from the user
    and displays that input back in upper and lower cases
"""

#testString = "Hayrulah"

def upperAndLower(string):
    print(string.upper()+ "\n" + string.lower())

#upperAndLower(testString)


#############################################################################################

"""
15. Write a Python function to create the HTML string with tags around the word(s).
Sample function and result : 
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
"""

def add_tags(tag, content):
    return "<%s>%s</%s>" % (tag, content, tag)


#print(add_tags("b", "Python"))


#############################################################################################

"""
16. Write a Python function to insert a string in the middle of a string.
Sample function and result : 
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
"""

def insert_string_middle(string, insert):
    newString = ""
    #finding middle value and turning to integer
    if len(string) % 2 == 0:
        middle = int(len(string) / 2)
        newString = string[:middle] + insert + string[middle:]
    return newString

#print(insert_string_middle("{{}}", "Python"))



#############################################################################################

"""
17. Write a Python function to get a string made of 4 copies of the last two characters
 of a specified string (length must be at least 2)
Sample function and result : 
insert_end('Python') -> onononon
insert_end('Exercises') -> eseseses
"""

def insert_end(string):
    newString = ""
    if len(string) < 2:
        newString = string
    else:
        lastTwoChars = string[-2: ]
        newString = lastTwoChars * 4

    return newString

#print(insert_end("Beray"))

#############################################################################################

"""
18. Write a Python function to get a string made of its first three characters
 of a specified string. If the length of the string is less than 3 
 then return the original string.
 
Sample function and result : 
first_three('ipy') -> ipy
first_three('python') -> pyt
"""

def first_three(string):
    newString = ""
    if len(string)<3:
        newString = string
    else:
        newString = string[:3]
    return newString

#print(first_three("python"))

#############################################################################################

"""  
19. Write a Python program to get the last part of a string
    before a specified character.
    
https://www.w3resource.com/python-exercises
https://www.w3resource.com/python
"""

def last_part(string):
    specified = "-"
    location = 0
    for i in range(len(string)):
        if specified == string[i]:
            location = i
    newString = string[:location]
    return newString

#print(last_part("https://www.w3resource.com/python-exercises"))

#############################################################################################


"""
20. Write a Python function to reverses a string if it's length is a multiple of 4
"""
name = "Beray"


def reverse_String(string):
    newString = ""
    if len(string) % 4 == 0:
        for i in range(len(string)-1, -1, -1):
            newString += string[i]
    return newString

#print(reverse_String(name))
