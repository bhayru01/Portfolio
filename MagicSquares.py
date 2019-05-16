"""
P6.20. Magic squares.
Write a program that reads in 16 values from the keyboard 
and tests whether they form a magic square when put into a 4 × 4 table.
You need to test two features:

1. Does each of the numbers 1, 2, ..., 16 occur in the user input?
2. When the numbers are put into a square, are the sums of the rows, columns,
and diagonals equal to each other?

"""

#
## The function requests to enter integers and adds them into table list
#  @param list, list table to insert the values in
#  @modifies the given list table
#
def fillTable(list):
    #Computing the total elements in the list
    totalElements = len(list) * len(list[0])
    print("Enter %2d integers" % totalElements)
    #for each row
    for i in range(len(list)):
        #for each element in the raw
        for j in range(len(list[0])):
            value = input("Enter a integer: ")
            #checking if entered value is integer
            while not value.isdigit():
                print("Error: Only digits !")
                value = input("Enter a integer: ")
            value = int(value)
            #assigning element
            list[i][j] = value


#
## The function creates a list table
# @param rows, columns to customize the dimension of the table list
# @return table list with default elements of 0
#
def createTable(rows, columns):
    table = []
    for i in range(rows):
        row = [0] * columns
        table.append(row)
    return table

#
## The function checks whether total of each rows are equal
# @param table, a table list to check for equality in sum of each row
# @return, if sum of each row equal, returns sum of a row, else returns -1
#
def isMagicRow(table):
    total = 0
    #A list for collecting if row is equal with True or False
    isEqual = []
    #for each row
    for i in range(len(table)):
        #assigning new variable for each total row
        totalRow = 0
        if i == 0:
            #for each element in the raw
            for j in range(len(table[0])):
                #computing the first raw for checking with other raws
                total += table[i][j]
                #assigning the totalRaw the same value
                totalRow = total
        else:
            for j in range(len(table[0])):
                totalRow += table[i][j]
        #Checking if first raw is equal to the any other raw
        #If it is add True to isEqual list else add False
        if total == totalRow:
            isEqual.append("True")
        else:
            isEqual.append("False")
        totalRow = 0
    #if there is False in isEqual list returns -1 else returns total
    if "False" in isEqual:
        total = -1
    return total


#
## The function checks whether each total columns are equal
# @param table, a table list to check for equality in sum of all columns
# @return, if sum of each column equal, returns sum of a column, else returns -1
#
def isMagicColumn(table):
    totalFirstColumn = 0
    # A list for collecting if row is equal with True or False
    isEqual = []
    total = 0
    #iterate over length size of the column
    for i in range(len(table[0])):
        # assigning new variable for each total column
        totalColumn = 0
        # for each row
        for row in table:
            #if this is the first element
            if i == 0:
                # computing the first column for checking with other columns
                totalFirstColumn += row[0]
                # assigning the totalColumn the same value, otherwise it will append false in the list
                totalColumn = totalFirstColumn
            else:
                totalColumn += row[i]
        # Checking if first column is equal to the any other column
        # If it is adds True to isEqual list else adds False strings
        if totalFirstColumn == totalColumn:
            isEqual.append("True")
        else:
            isEqual.append("False")
    # if there is False in isEqual list returns -1 else returns total
    if "False" in isEqual:
        total = -1
    else:
        total = totalFirstColumn
    return total



def isMagicDiagonal(table):
    totalFirstDiagonal = 0
    totalSecondDiagonal = 0
    total = -1
    for i in range(len(table)):
        totalFirstDiagonal += table[i][i]
    for i in range(len(table)-1, -1, -1):
        totalSecondDiagonal += table[i][i]
    if totalFirstDiagonal == totalSecondDiagonal:
        total = totalSecondDiagonal
    return total




def main():

    table = createTable(4, 4)
    fillTable(table)
    row = isMagicRow(table)
    column = isMagicColumn(table)
    diagonal = isMagicDiagonal(table)

    if row == column and row == diagonal and row != -1:
        print( "It is Magic Square !!!")
    else:
        print("NOT Magic Square ! ")
main()
