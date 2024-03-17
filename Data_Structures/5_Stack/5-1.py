# ## Data structure tutorial exercise: Stack
# 1. Write a function in python that can reverse a string using stack data structure. 
# Use [Stack class](https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/5_Stack/5_stack.ipynb) from the tutorial.
#     ```
#     reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
#     ```

from collections import deque
stack = deque()

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    

# Rohan's Version -> using generic Python
# def reverse_string(str):
#     reversed_str = ''
#     for char in str:
#         reversed_str = char + reversed_str
#     return reversed_str
    
def reverse_string(str):
    s = Stack()

    # take each char in the inputted string and add it to the stack

    for char in str:
        s.push(char)
    
    # now pop out each char and add to the output string
    reversed_str = ''
    for i in range(len(s.container)):
        reversed_str = reversed_str + s.pop()

    return reversed_str

    
# Keys
    # 1. Don't define the method within the Stack class. We want to apply it using the stack class
    # 2. Use the stack methods
    

s = Stack()
s.push("https://www.cnn.com/")
s.pop()

s.push(9)
s.push(34)
s.push(78)
s.push(12)

print(s.peek())

s.pop()

print(s.peek())

print(reverse_string("We will conquere COVID-19"))

print(reverse_string("hello Rohan"))