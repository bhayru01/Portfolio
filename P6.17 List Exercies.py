"""
P6.17.
Make a second list and fill it with the numbers 1 to 10.
Repeat 10 times
    Pick a random element from the second list.
    Remove it and append it to the permutation list.
"""


def mainFunction():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    permutation = []
    for i in range(10):
        randomElement = randomChoice(numbers)
        permutation.append(randomElement)
    print(permutation)


#
##Function selects random elements from the list
# @param list, the list that random elements is taken from
# @return, returns randomly selected element, and removes it from the list
#
def randomChoice(list):
    from random import randint
    randomPos = randint(0, len(list)-1)
    randomElement = list.pop(randomPos)
    return randomElement



mainFunction()
