####### File Exercise from the book "Python For Everyone" by Horstmann #######

"""
    
Write a program that asks the user to input a set of floating-point values.
When the user enters a value that is not a number,
give the user a second chance to enter the value.
After two chances, quit reading input.
Add all correctly specified values and
print the sum when the user is done entering data.
Use exception handling to detect improper inputs.
    
"""

## The Function checks wheter n is float or not
# @param n, element to check
# @return, returns True Or False
#
def is_float(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


## The Function asks to enter floats and returns it, if it is not - raises an ValueError
# @return, returns a floating point number
#
def enterFloats():
    number = input("Enter a Float: ")
    # Checking the number with is_float function
    if is_float(number):
        number = float(number)
        return number
    else:
        raise ValueError("Error: Digits only !")


def main():
    #counting the wrong entered values
    mistakes = 0
    #limiting the wrong entered values
    limit = 2
    #summing the total entered float numbers
    total = 0

    #when wrong entered values is less than limited wrong values
    while mistakes < limit:
        #handling exceptions
        try:
            digit = enterFloats()
            # summing float values
            total += digit
        except ValueError as exception:
            print(str(exception))
            #when value is not float increasing mistakes by one
            mistakes += 1


    #printing total sum after has been entered two wrong values
    print(total)


main()
