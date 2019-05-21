####### File Exercise from the book "Python For Everyone" by Horstmann #######
"""

p7.4
  Write a program that reads a file containing two columns of floating-point numbers.
  Prompt the user for the file name.
  Print the average of each column.

"""

file = open("input.txt", "w")
print("2 1\n3 2\n4 3\n6 8\n9 4", file=file)
file.close()

def averageColumn(file):
    totalFirst = 0.0
    totalSecond = 0.0
    wholeFile = file.readlines()
    for i in range(len(wholeFile)):
        line = wholeFile[i].split()
        totalFirst += float(line[0])
        totalSecond += float(line[1])
    averageFirstColumn = totalFirst / len(wholeFile)
    averageSecondColumn = totalSecond / len(wholeFile)

    print("Average First Column: %.2f\nAverage Second Column: %.2f" % (averageFirstColumn, averageSecondColumn ))

userInput = input("Enter text file name: ")
openFile = open(userInput, "r")
averageColumn(openFile)
openFile.close()
