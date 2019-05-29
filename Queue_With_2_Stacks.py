"""
Implement a Queue - Using Two Stacks

Use a Python list data structure as your Stack.

"""
##This class implements a Queue using two Stacks
#
class Queue2Stacks():

    def __init__(self):
        self._stack1 = []
        self._stack2 = []

    def enqueue(self, element):

        self._stack1.append(element) # APPENDING ELEMENT TO THE FIRST STACK

    def dequeue(self):

        if len(self._stack2) == 0: #IF STACK2 IS EMPTY
            while len(self._stack1) > 0: # WHILE STACK1 IS FULL
                self._stack2.append(self._stack1.pop()) # APPENDING ELEMENT FROM STACK1 TO STACK2

        #RETURNING THE ELEMENT FROM STACK2
        return self._stack2.pop()



### TESTING ###
q = Queue2Stacks()
for i in range(1, 6): #ADDING ELEMENTS FROM 1 TO 5
    q.enqueue(i)

for i in range(1, 6):
    print(q.dequeue()) # EXPECTED FROM 1 TO 5 IN ASCENDING ORDER
