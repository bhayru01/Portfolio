"""

P6.8 Compute the alternating sum of all elements in a list.
    For example, if your program reads the input
    1 4 9 16 9 7 4 9 11
    then it computes
    1–4+9–16+9–7+4–9+11=–2

"""
numbers = [1, 4, 9, 16, 9, 7, 4, 9, 11]

#
##The function returns alternating sum of the given list
# @param list, list to compute alternating sum
# @return, returns alternating sum
#
def alterSum(list):
    total = 0
    for i in range(len(numbers)):
        if i % 2 == 0 :
            total += numbers[i]
        else:
            total -= numbers[i]
    return total

print(alterSum(numbers))
