"""
Unique Characters in String
Problem

Given a string,determine if it is compreised of all unique characters. 
For example, the string 'abcde' has all unique characters and should return True. 
The string 'aabcde' contains duplicate characters and should return false.

"""

test1 = "abcde"
test2 = "aabcde"

## THE FUNCTION CHECKS IF STRING CONSISTS WITH UNIQUE ELEMENTS, USING DICTIONARY
# @param string to check for unique elements
# @return True or False for unique elemetns
#
def uni_char(string):
    dictionary = dict()

    for element in string:
        if element in dictionary:
            dictionary[element] += 1
        else:
            dictionary[element] = 1

    for key in dictionary:
        if dictionary[key] > 1:
            return False
        else:
            return True

print(uni_char(test2))


#---------------------------#
## THE FUNCTION CHECKS IF STRING CONSISTS WITH UNIQUE ELEMENTS, USING SET DATA STRUCTURE
# @param string to check for unique elements
# @return True or False for unique elemetns
#
def uni_char2(string):
    return len(set(string)) == len(string)

print(uni_char2(test2))
