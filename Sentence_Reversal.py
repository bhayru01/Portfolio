""" 
Sentence Reversal
Problem
Given a string of words, reverse all the words. For example:

Given:

'This is the best'

Return:

'best the is This'

As part of this exercise you should remove all leading and trailing whitespace. 
So that inputs such as:

'  space here'  and 'space here      '

both become:

'here space'

"""

## THIS FUNCTION REVERSES WORDS
## USING PYTHON METHODS .strip() and .split()
# @param string to reverse
# @return reversed WORDS
#
# Time complexity O(N) and O(N) space complexity
#
def rev_word(string):
    string = string.strip() #REMOVING WHITE SPACES FROM THE SIDES
    string = string.split() #MAKING ARRAY
    newString = "" #ASSIGNING EMPTY STRING TO ADD REVERSED WORDS

    #STARTING FROM THE LAST POSITION OF THE ARRAY
    for i in range(len(string)-1, -1, -1):
        newString = newString + " " + string[i] #ADDING WORDS TO THE STRING VARIABLE AND SPACE BETWEEN THEM
        newString = newString.strip() #REMOVING THE WHITE SPACES FROM THE REVERSED STRING VARIABLE
    return newString


#-----------#

## THIS FUNCTION REVERSES WORDS
## USING STACK DATA STRUCTURE
# @param string to reverse
# @return reversed WORDS
#
# Time complexity O(N) and O(N) space complexity
#
def rev_word(string):

    from Stack import ArrayStack  # STACK IMPORTED FROM MY OWN COLLECTION

    stack = ArrayStack() # ASSIGNING NEW STACK
    reversedWords = "" # ASSIGNING NEW STRING, WILL BE ADDED REVERSED WORDS IN HERE LATER ON
    word = "" #ASSIGNING NEW STRING, SO IT CAN ADD EACH WORD

    #I AM ADDING A WHITE SPACE AT THE END OF THE STRING
    #SO THE LOOP CAN UNDERSTAND THE END OF THE STRING
    #IF I DONT ADD THIS, THE PROGRAM WILL NOT PUT THE LAST WORD IN THE STACK !
    string = string + " "


    for i in range(len(string)): #FOR EACH ELEMENT IN THE STRING
        if string[i] != " ": #IF CHAR NOT A WHITE SPACE ADD CHARS TO THE WORD
            word += string[i]
        else:
            if len(word) > 0: #IF THE LENGTH OF THE WORD MORE THAN ZERO
                stack.push(word) #ADD WORD TO THE STACK
                word = "" #CLEAR WORD VARIABLE, FOR THE NEXT ONE


    for i in range(len(stack)):
        reversedWords += stack.pop() + " " #ADDING EACH ELEMENT TO THE reversedWords STRING WITH SPACE BETWEEN WORDS
    reversedWords = reversedWords[:-1] #REMOVING THE LAST ELEMENT OF THE STRING, BECAUSE IT IS A WHITE SPACE. ADDED FROM THE PREVIOUS LINE
    return reversedWords


test1 = '  space here' #EXPECTED: 'here space'
test2 = 'Hi John,   are you ready to go?' #EXPECTED: 'go? to ready you are John, Hi'
test3 = '   Hello John    how are you   ' #EXPECTED: 'you are how John Hello'
test4 = '1' #EXPECTED '1'
print(rev_word(test1))
