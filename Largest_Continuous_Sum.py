"""
Largest Continuous Sum
Problem
Given an array of integers (positive and negative) 
find the largest continuous sum.

"""

##THIS FUNCTION RETURNS THE SUM OF LONGEST CONTINUOUS SUM OF THE LIST
# @param arr to calculate the sum
# @return max_sum, the longest continuous sum
#
def large_cont_sum(arr):
    if len(arr) == 0: #if the length of the array equal zero return o
        return 0

    current_sum = arr[0] #assigning the current_sum to the first element of the array
    max_sum = current_sum # assigning max_sum to current_sum by default

    # starting from the second element of the array
    for element in arr[1:]:

        #Choosing the max value between (current_sum + element) and element
        # and assigning to the variable current_sum
        current_sum = max(current_sum+element, element)

        # Choosing the max value between current_sum and max_sum
        # and assigning to the variable max_sum
        max_sum = max(current_sum, max_sum)

    return max_sum

arr = [-1, -2, 1, -5]
print(large_cont_sum(arr))
