"""

Balanced Parentheses Check - SOLUTION
Problem Statement
Given a string of opening and closing parentheses, check whether it’s balanced. 
We have 3 types of parentheses: round brackets: (), square brackets: [], 
and curly brackets: {}. 
Assume that the string doesn’t contain any other character than these, 
no spaces words or numbers. 
As a reminder, balanced parentheses require every opening parenthesis 
to be closed in the reverse order opened. 

For example ‘([])’ is balanced but ‘([)]’ is not.

You can assume the input string has no spaces.

"""


## THIS FUNCTION CHECKS WHETHER STRING HAS BALANCED PARENTHESES
# @param string to check
# @return True or False
#
#TIME COMPLEXITY O(N)
def balance_check(string):

    openingBrackets = "[({"
    closingBrackets = "])}"
    isBalanced = False

    stack = ArrayStack() #STACK IS IMPORTED FROM MINE COLLECTION

    for element in string: #FOR EACH ELEMENT IN STRING
        if element in openingBrackets: #IF openingBrackets
            stack.push(element) # PUSH TO stack
        elif element in closingBrackets: # IF closingBrackets
            if stack.isEmpty(): #CHECKING FIRST IF stack is empty
                return False
            else:
                lastElement = stack.pop() #GETTING THE LAST ELEMENT FROM stack
                openPos = openingBrackets.find(lastElement) #GETTING ITS POSITION IN openingBrackets variable
                closePos = closingBrackets.find(element) #GETTING CURRENT ELEMENT POSITION FROM closingBrackets VARIABLE
                if openPos != closePos: #IF POSITIONS OF BOTH VARIABLE NOT EQUAL RETURN FALSE
                    return False
                else:
                    isBalanced = True #OTHERWISE MAKE isBalanced True
        if len(stack) > 0: #IF STACK NOT EMPTY isBalanced = FALSE
            isBalanced = False
    return isBalanced

test1 = "[]"
test2 = "[](){([[[]]])}"
test3 = '[{{{(())}}}]((()))'
test4 = "()(){]}"
test5 = '[](){([[[]]])}('
test6 = '[[[]])]'

print("Test 1:", balance_check(test1)) # EXPECTED TRUE
print("Test 2:", balance_check(test2)) # EXPECTED TRUE
print("Test 3:", balance_check(test3)) # EXPECTED TRUE
print("Test 4:", balance_check(test4)) # EXPECTED FALSE
print("Test 5:", balance_check(test5)) # EXPECTED FALSE
print("Test 6:", balance_check(test6)) # EXPECTED FALSE
