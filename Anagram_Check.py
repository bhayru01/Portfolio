"""
Problem

Given two strings, check to see if they are anagrams. 
An anagram is when the two strings can be written using the exact same letters 
(so you can just rearrange the letters to get a different phrase or word).

For example:

"public relations" is an anagram of "crap built on lies."

"clint eastwood" is an anagram of "old west action"

"""


#TEST VARIABLES
s1 = "d     o d"
s2 = "God"

s3 = "clint eastwood"
s4 = "old west action"

s5 = "aa"
s6 = "bb"


## This fucntion checks if two strings are Anagram by using list
# @param s1, s2 to check wheter they are anagrams
# @return if anagram True else False
# O(N2) TIME COMPLEXITY
#
def anagram(s1, s2):
    isAnagram = False
    #REMOVING WHITE SPACES AND MAKING UPPER CASE BOTH STRINGS
    s1 = s1.replace(" ", "").upper()
    s2 = s2.replace(" ", "").upper()
    if len(s1) != len(s2): #RETURN FALSE IF THE LENGTH OF BOTH STRING NOT EQUAL
        return False
    else:
        for i in range(len(s1)):
            if s1[i] not in s2: #CHECKING IF ELEMENTS IN S1 IN S2, IF NOT RETURN FALSE
                return False
            elif s2[i] not in s1: #CHECKING IF ELEMENTS IN S2 IN S1, IF NOT RETURN FALSE
                return False
            else:
                isAnagram = True #OTHERWISE ANAGRAM IS TRUE
    return isAnagram


print(anagram(s1, s2))


##############################################################################


## This fucntion checks if two strings are Anagram by using dictionary
# @param s1, s2 to check wheter they are anagrams
# @return if anagram True else False
# O(N2) TIME COMPLEXITY
#
def anagram2(s1, s2):
    # REMOVING WHITE SPACES AND MAKING UPPER CASE BOTH STRINGS
    s1 = s1.replace(" ", "").upper()
    s2 = s2.replace(" ", "").upper()
    if len(s1) != len(s2):  # RETURN FALSE IF THE LENGTH OF BOTH STRING NOT EQUAL
        return False

    #ASSIGNING DICTIONARY TO COUNT THE LETTERS
    count = dict()


    #FOR EACH ELEMENT IN S1, CHECKING IF IT IS IN DICTIONARY count
    # IF IT IS INCREASE BY ONE ITS VALUE
    # ELSE ASSIGN 1
    for element in s1:
        if element in count:
            count[element] += 1
        else:
            count[element] = 1

    # FOR EACH ELEMENT IN S2, CHECKING IF IT IS IN DICTIONARY count
    # IF IT IS DECREASE BY ONE ITS VALUE
    # ELSE ASSIGN 1
    for element in s2:
        if element in count:
            count[element] -= 1
        else:
            count[element] = 1

    #FOR EACH KEY IN DICTIONARY COUNT
    for key in count:
        #IF VALUE OF EACH KEY NOT EQUAL TO 0 RETURN FALSE, "NOT ANAGRAM"
        if count[key] != 0:
            return False

    #IF ALL PASSED RETURN TRUE, "IT IS ANAGRAM"
    return True


print(anagram2(s3, s4))



##############################################################################


## This fucntion checks if two strings are Anagram by sorting both strings and comparing with equality
# @param s1, s2 to check wheter they are anagrams
# @return, if sorted string1 is equal to sorted string2 returns True, False otherwise
#
def anagram3(s1, s2):
    # REMOVING WHITE SPACES AND MAKING UPPER CASE BOTH STRINGS
    s1 = s1.replace(" ", "").upper()
    s2 = s2.replace(" ", "").upper()

    #COMPARE BOTH SORTED STRINGS IF THEY ARE EQUAL
    return sorted(s1) == sorted(s2)

print(anagram3(s5, s6))
