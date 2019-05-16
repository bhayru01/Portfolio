"""
P6.9
Write a function that reverses the sequence of elements in a list.
For example, if you call the function with the list

1 4 9 16 9 7 4 9 11
then the list is changed to
11 9 4 7 9 16 9 4 1
"""

list = [1, 4, 9, 16, 9, 7, 4, 9, 11]

#
## The Function modifies with reversing a list
# @param list, list to reverse
#
def reverseList(list):
    pos = 0
    #finding the last element position
    lastElementPos = len(list) - 1

    #finding the middle element position depending on its length
    if len(list) % 2 == 0:
        middleElementPos = (len(list)//2) - 1
    else:
        middleElementPos = len(list)//2

    #Reversing the list
    for i in range(lastElementPos, middleElementPos, -1):
        #tempory variable to swap elements
        temp = list[pos]
        list[pos] = list[i]
        list[i] = temp
        pos += 1

reverseList(list)
print(list)
