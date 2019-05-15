####### Function Exercises from the book "Python For Everyone" by Horstmann #######

#
##Computing the larger of two integers
#
def larger(first, second):
    larger = 0
    if first > second:
        larger = first
    else:
        larger = second
    return larger


#------------------------------------------------------------------------------#

#
##Computing the smallest of three floating-point numbers
#
def smallest(first, second, third):
    smallest = first
    if first <= smallest:
        smallest = first
    if second <= smallest:
        smallest = second
    if third <= smallest:
        smallest = third
    return smallest


#------------------------------------------------------------------------------#

#
##Checking whether an integer is a prime number,
# returning True if it is and False otherwise
#
def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


#------------------------------------------------------------------------------#

#
##Checking whether a string is contained inside another string
#
#Here I used nested loop to check substring in a string
# I have also checked the previous letters of both strings
# to make sure that it is a one word not separate letters in the string
# When they are equal I put them in a new string
# And check them whether new string and the substring is equal

def searchString(string, substring):

    newName = substring[0]

    for i in range(1, len(substring)):
        previousI = substring[i - 1]
        for j in range(1, len(string)):
            previousJ = string[j-1]
            if substring[i] == string[j] and previousI == previousJ:
                newName += substring[i]

    if newName == substring:
        return True
    else:
        return False

#------------------------------------------------------------------------------#

#
##Computing the balance of an account with a given initial balance,
# an annual interest rate, and a number of years of earning interest
#

def computingBalance(balance, rate, year):
    for i in range(year):
        interest = balance * rate
        balance = balance + interest
        print("Year: %2d , Balance: %2.2f" % (i+1, balance))



#------------------------------------------------------------------------------#


#
##Printing the calendar for a given month and year
#
def viewCalendar(y, m):
    import calendar
    print(calendar.month(y, m))



#------------------------------------------------------------------------------#

#
##Computing the day of the week for a given day, month, and year
# (as a string such as "Monday")
#

def dayOftheWeek(year, month, day):
    import calendar
    day = calendar.weekday(year, month, day)
    if day == 0:
        print("Monday")
    elif day == 1:
        print("Tuesday")
    elif day == 2:
        print("Wednesday")
    elif day == 3:
        print("Thursday")
    elif day == 4:
        print("Friday")
    elif day == 5:
        print("Saturday")
    elif day == 6:
        print("Sunday")
    else:
        print("Error: Wrong Input!")



#------------------------------------------------------------------------------#

#
## Generating a random integer between 1 and n
#
def randomInteger(number):
    from random import randint
    randomNumber = randint(1, number)
    print(randomNumber)


#------------------------------------------------------------------------------#



#
## Write a function
## def repeat(string, n, delim)
## that returns the string string repeated n times,
## separated by the string delim.
## For example, repeat("ho", 3, ", ") returns "ho, ho, ho".
#
def repeat(string, n, delim):
    newString = ""
    for i in range(n):
        newString += string
        if i < n-1:
            newString += delim
    return newString

#------------------------------------------------------------------------------#



## The program constructs a scrambled version of a given word,
# randomly flips two characters other than the first and last one.
# and then the program reads words and prints the scrambled words.


#Asking user to enter any string
#string = input("Enter sentence: ")

#Calling the main function
#main()



## main function prints scrambled string from the user input
# @param string, string to scramble each word using scramble function
# and concatenating all the scrambled words in new string
#
# @print newString, printing new Scrambled String
#
def main(string):
    word = ""
    newString = ""
    for i in range(len(string)):
        if string[i] != " ":
            word += string[i]
        if string[i] == " " or i == len(string)-1:
            scrambledWord = scramble(word)
            newString = newString + scrambledWord + " "
            word = ""
    print(newString)


## The function scramble(word)constructs a scrambled version of a given word
# @param word, word to scramble except first and last character
# @return scrambleWord, modified scrambled newWord
def scramble(word):
    scrambleWord = ""
    if len(word)<4:
        scrambleWord = word
    else:
        #IMPORTING RANDOM NUMBERS
        from random import randint

        #GETTING 2 RANDOM NUMBERS WITHOUT FIRST AND LAST FROM THE WORD
        randomNumber1 = randint(1, len(word)-2)
        randomNumber2 = randint(1, len(word)-2)

        #IF THEY ARE EQUAL KEEP GETTING NEW RANDOM NUMBER
        while randomNumber1 == randomNumber2:
            randomNumber2 = randint(1, len(word)-2)
        #WHAT HAPPENS IF THE WORD IS WITH 3 OR LESS LETTERS!!!

        #NEW EMPTY STRING TO CONCATONATE THE MODIFIED LETTERS
        #scrambleWord = ""

        #SWAPPING AND CONCATINATING CHARACTERS IN THE WORD TO NEW
        for i in range(len(word)):
            if i == randomNumber1:
                scrambleWord += word[randomNumber2]
            elif i == randomNumber2:
                scrambleWord += word[randomNumber1]
            else:
                scrambleWord += word[i]

    return scrambleWord

#------------------------------------------------------------------------------#


##The Function tests whether the year is Leap or not
# @param year, year to test
# @return True or False
def isLeapYear(year):

    import calendar
    month = calendar.month(year, 2)
    leapDay = "29"

    if leapDay in month:
        return True
    else:
        return False


#------------------------------------------------------------------------------#




#specialCharacter = "+-*/?!@#$%&"
#letters_lower = 'abcdefghijklmnopqrstuvwxyz'
#letters_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#digits = '0123456789'



##The function returns random lower letter
# @param letters_lower, all the letters in lower case in one string
# @return, random lower case letter
def randomLower(letters_lower):
    from random import randint
    randomNum = randint(0, len(letters_lower)-1)
    randomLower = letters_lower[randomNum]
    return randomLower


##The function returns random upper letter
# @param letters_upper, all the letters in upper case in one string
# @return, random upper case letter
def randomUpper(letters_upper):
    from random import randint
    randomNum = randint(0, len(letters_upper)-1)
    randomUpper = letters_upper[randomNum]
    return randomUpper


##The function returns random charachter
# @param specialCharacter, all the special characters in one string
# @return random character
def randomChar(specialCharacter):
    from random import randint
    randomNum = randint(0, len(specialCharacter)-1)
    randomChar = specialCharacter[randomNum]
    return randomChar


##The function returns random digit
# @param digits, all the digits in one string
# @return random digit
def randomDigit(digits):
    from random import randint
    randomNum = randint(0, len(digits)-1)
    randomDigit = digits[randomNum]
    return randomDigit


##The function generates random string with 8 characters
# (5: lower letters, 1: upper letter, 1: digit, 1: special character)
# @param specialCharacter, Included special characters
# @param letters_upper, all english alphabet upper case letters
# @param letters_lower, all english alphabet lower case letters
# @param digits, digits from 0-9 in string format
# return, random 8 characters password in string format
def generatePassword(specialCharacter, letters_upper, letters_lower, digits):

    from random import randint
    password = ""

    #adding random choiced digits
    randomLimited = ""


    #generating 8 characters string
    for i in range(8):
        #generating random numbers from 1 to 4
        randomNum = randint(1, 4)

        #converting random number into string
        randomNumString = str(randomNum)

        # checking if random number once added to the password
        # and if the random number is 4
        if randomNumString not in randomLimited and randomNumString != str(4):
            if randomNum == 1:

                # assigning upper case letter from randomUpper function
                letterUpper = randomUpper(letters_upper)

                # adding to the password string
                password += letterUpper

                # adding this number to the randomLimited variable
                randomLimited += str(randomNum)
            elif randomNum == 2:

                # assigning special character from randomChar function
                specialChar = randomChar(specialCharacter)

                # adding to the password string
                password += specialChar

                # adding this number to the randomLimited variable
                randomLimited += str(randomNum)
            elif randomNum == 3:

                # assigning random digit from randomDigit function
                digit = randomDigit(digits)

                # adding to the password string
                password += digit

                # adding this number to the randomLimited variable
                randomLimited += str(randomNum)
        else:

            # assigning lower case letter from randomLower function
            letterLower = randomLower(letters_lower)

            # adding to the password string
            password += letterLower

    # returning random password
    return password



## Function prints random Password with 8 characters
#
def printPassword():
    password = generatePassword(specialCharacter, letters_upper, letters_lower,digits)
    print(password)



def printTriangle(sideLength) :
    if sideLength < 1 : return
    printTriangle(sideLength - 1)
    print("[]" * sideLength)

#printTriangle(1)



def printTriangle(sideLength):
    if sideLength < 1 : return
    print("[]" * sideLength)
    printTriangle(sideLength - 1)

#printTriangle(4)

def mystery(n) :
    if n <= 0 : return 0
    return n + mystery(n - 1)
