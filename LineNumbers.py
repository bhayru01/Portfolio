####### File Exercise from the book "Python For Everyone" by Horstmann #######
"""
p7.2 
Write a program that reads a file containing text.
Read each line and send it to the output file, preceded by line numbers.
If the input file is:

    Mary had a little lamb
    Whose fleece was white as snow.
    And everywhere that Mary went,
    The lamb was sure to go!
    
then the program produces the output file:

/* 1 */ Mary had a little lamb
/* 2 */ Whose fleece was white as snow. 
/* 3 */ And everywhere that Mary went, 
/* 4 */ The lamb was sure to go!
"""

file = open("input.txt", "w")
file.write("Mary had a little lamb\nWhose fleece was white as snow.\nAnd everywhere that Mary went,\nThe lamb was sure to go!")
file.close()

# SAME OUTPUTS WITH DIFFERENT IMPLEMENTATIONS

# READING AND PRINTING WITH WHILE LOOP
def printNewFile(file):
    i = 1
    #reading the line
    text = file.readline()
    while text != "":
        # removing the white spaces at the end
        text = text.rstrip()
        print("/* %d */ %s" % (i, text))
        text = file.readline()
        i += 1

# READING AND PRINTING WITH FOOR LOOP
def printNewFile2(file):
    i = 1
    for line in file:
        line  = line.rstrip()
        print("/* %d */ %s" % (i, line))
        i += 1


# PUTTING THE FILE INTO LIST THEN PRINTING EACH LINE
def printNewFile3(file):
    #making the whole file into list
    text = file.readlines()
    for i in range(len(text)):
        print("/* %d */ %s" % (i+1, text[i].rstrip()))

openFile = open("input.txt", "r")
printNewFile3(openFile)
openFile.close()
