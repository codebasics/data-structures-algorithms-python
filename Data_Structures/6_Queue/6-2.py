# 2. Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main tutorial.
# Binary sequence should look like,
# ```
#     1
#     10
#     11
#     100
#     101
#     110
#     111
#     1000
#     1001
#     1010
# ```
# Hint: Notice a pattern above. After 1 second and third number is 1+0 and 1+1. 4th and 5th number are second number (i.e. 10) + 0 and second number (i.e. 10) + 1.

# You also need to add front() function in queue class that can return the front element in the queue.

from collections import deque

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    
#     def front(self):
#         return self.buffer[-1]

# def produce_binary_numbers(n):
#     numbers_queue = Queue()
#     numbers_queue.enqueue("1")

#     for i in range(n):
#         front = numbers_queue.front()
#         print("   ", front)
#         numbers_queue.enqueue(front + "0")
#         numbers_queue.enqueue(front + "1")

#         numbers_queue.dequeue()

# produce_binary_numbers(10)

# Rohan's solution
    
# q = Queue()

# for i in range(1,11):
#     q.enqueue(bin(i))

# while q.is_empty() == False:
#     print(q.dequeue().replace('0b',''))
    
#Rohan's solution V2
    
def produce_binary_numbers(n):
    numbers_queue = Queue()

    for i in range(1,(n+1)):
        numbers_queue.enqueue(bin(i))

    while numbers_queue.is_empty() == False:
        print(numbers_queue.dequeue().replace('0b',''))

produce_binary_numbers(10)


