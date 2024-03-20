# 2. Write a function in python that checks if paranthesis in the string are balanced or not. 
# Possible parantheses are "{}',"()" or "[]". 
# Use [Stack class](https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/5_Stack/5_stack.ipynb) from the tutorial.
#     ```
#     is_balanced("({a+b})")     --> True
#     is_balanced("))((a+b}{")   --> False
#     is_balanced("((a+b))")     --> True
#     is_balanced("))")          --> False
#     is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True

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
    

#Idea 1
    # run through each char, add to the Stack if it's a [, ], {, }, (, or )
    # create a counter for {}s, []s, and ()s. Increment by 1 if a [, {, or ( is popped out. Decrement by 1 if a ], }, or ) is popped out. 
    
    # if a ), ], or } shows up before a (, [, or { return false

def is_balanced(str):
    s = Stack()

     # run through each char, add to the Stack if it's a [, ], {, }, (, or )
    for char in str:
        if char == '[' or char == ']' or char == '{' or char == '}' or char == '(' or char == ')':
            s.push(char)

    # print(s.size())
    # for i in range(s.size()):
    #     print(s.pop())
    
    # create a counter for {}s, []s, and ()s. Increment by 1 if a [, {, or ( is popped out. 
    #Decrement by 1 if a ], }, or ) is popped out. 
    sq_bracket_counter = 0
    crly_bracket_counter = 0
    parenthesis_counter = 0

    for i in range(s.size()):
        character = s.pop()
        if character == "[":
            sq_bracket_counter +=1
        elif character == "]":
            sq_bracket_counter -=1
        if character == "{":
            crly_bracket_counter +=1
        elif character == "}":
            crly_bracket_counter -=1
        if character == "(":
            parenthesis_counter +=1
        elif character == ")":
            parenthesis_counter -=1

        # if a ), ], or } shows up before a (, [, or { return false -> this will cause a counter to go positive
        if sq_bracket_counter > 0 or crly_bracket_counter > 0 or parenthesis_counter > 0:
            return False
    
    # Once done, check the final counts
        
    # if all 3 equal 0 at the end, return True. Else return false
    if sq_bracket_counter == 0 and crly_bracket_counter == 0 and parenthesis_counter == 0:
        return True
    else:
        return False
    
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))

    