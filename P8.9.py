"""
P8.9
Write a program that asks a user to type in two strings and that prints
• the characters that occur in both strings.
• the characters that occur in one string but not the other.
• the letters that don’t occur in either string.
Use the set function to turn a string into a set of characters.

"""
def main():
    string1 = input("Enter string1: ")
    string2 = input("Enter string2: ")

    set1 = set(string1)
    set2 = set(string2)

    print("The characters that occur in both strings:")
    printIntersection(set1, set2)
    print()

    print("The characters that occur in one string but not the other:")
    printDifference(set1, set2)
    print()

    print("The letters that don’t occur in either string:")
    printNotIntersection(set1, set2)

## The function prints chars occurs in both sets
# @param set1, a set containing characters to modify
# @param set2, a set containging characters to modify
#
def printIntersection(set1, set2):
    intersection = set1.intersection(set2)
    for char in sorted(intersection):
        print(char)

## The function prints chars occurs in one set but not the other
# @param set1, a set containing characters to modify
# @param set2, a set containging characters to modify
#
def printDifference(set1, set2):
    difference = set1.difference(set2)
    for char in difference:
        print(char)

## The function prints chars that don’t occur in either set
# @param set1, a set containing characters to modify
# @param set2, a set containging characters to modify
#
def printNotIntersection(set1, set2):
    allChars = set1.union(set2)
    intersection = set1.intersection(set2)
    notInersection = allChars.difference(intersection)
    for char in notInersection:
        print(char)
