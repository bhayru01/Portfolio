"""
Find the Missing Element
Problem

Consider an array of non-negative integers. 
A second array is formed by shuffling the elements of the first array 
and deleting a random element. 
Given these two arrays, find which element is missing in the second array.

Here is an example input, the first array is shuffled 
and the number 5 is removed to construct the second array.

Input:

finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output:

5 is the missing number


"""

## TEST CASES ##
#arr1 = [1, 2, 3, 4, 5, 6, 7]
#arr2 = [3, 7, 2, 1, 4, 6]

#arr1 = [5, 5, 7, 7]
#arr2 = [5, 7, 7]

arr1 = [9,8,7,6,5,4,3,2,1]
arr2 = [9,8,7,5,4,3,2,1]

##THIS FUNCTIONS COMPARES TWO LISTS AND FINDS THE MISSING ELEMENT FROM THE SECOND LIST IF THERE IS.
# @param arr1, a list to compare with its values with other list
# @param arr2, a list to check wheter its values are missing compare to arr1
# @return missing value from arr2 comparing with arr1
# O(N) time complexity, O(N) space complexity
# THIS APRROACH COULD BE PROBLEMATIC IF THE ARRAYS ARE TOO LARGE
# BETTER VERSION BELLOW
#
def findMissingValue(arr1, arr2):
    seen = dict() # setting an dictionary object
    if len(arr1) <= len(arr2): # returning error message if the length of arr2 more than or equal to arr1
        return print("Error: the length of the arr2 must be less than arr1")

    #FOR EVERY ELEMENT IN ARR1 ADDING ITS ELEMENTS TO DICTIONARY AS KEY
    # AND AS A VALUE INCREASING BY 1 IF ALREADY EXISTS IN THE DICTIONARY
    #
    for i in range(len(arr1)):
        if arr1[i] in seen:
            seen[arr1[i]] += 1
        else:
            seen[arr1[i]] = 1

    # FOR EVERY ELEMENT IN ARR2 ADDING ITS ELEMENTS TO DICTIONARY AS KEY
    # AND AS A VALUE DECREASING BY 1 IF ALREADY EXISTS IN THE DICTIONARY
    #
    for i in range(len(arr2)):
        if arr2[i] in seen:
            seen[arr2[i]] -= 1
        else:
            seen[arr2[i]] = 1

    # BY THIS ALGORITHM IF THERE IS NO MISSING ELEMENT
    # EVERY KEY WILL HAVE 0 AS A VALUE
    # OTHERWISE MORE THAN ZERO VALUE, ITS KEY WILL BE THE MISSING ELEMENT
    #
    for key in seen:
        if seen[key] != 0:
            return key

#print(findMissingValue(arr1, arr2))

#-----------------------------------#
##ANOTHER FUNCTIONS WHERE COMPARES TWO LISTS AND FINDS THE MISSING ELEMENT FROM THE SECOND LIST IF THERE IS.
# @param arr1, a list to add all its values to the total instance variable
# @param arr2, a list to substract all its values to the total instance variable
# @return total variable, where its added first and substract after
# O(N) time complexity, O(1) space complexity
#
def findMissingValue2(arr1, arr2):

    total = 0
    for num in arr1:
        total += num
    for num2 in arr2:
        total -= num
    return total
