# ## Data structure tutorial exercise: Queue

# For all exercises use [Queue class](https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/6_Queue/6_queue.ipynb) implemented in main tutorial.

# 1. Design a food ordering system where your python program will run two threads,
#     1. Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
#     1. Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.

#     Use this video to get yourself familiar with [multithreading in python](https://www.youtube.com/watch?v=PJ4t2U15ACo&list=PLeo1K3hjS3uub3PRhdoCTY8BxMKSW7RjN&index=2&t=0s)

#     Pass following list as an argument to place order thread,
#     ```
#     orders = ['pizza','samosa','pasta','biryani','burger']
#     ```
#     This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order thread is consuming the food orders.
#     Use Queue class implemented in a video tutorial.

from collections import deque

import time # so we can run a delay
import threading # so we can multithread

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, waiting for orders...")
            return None
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    
def place_order(queue, orders):
    for order in orders:
        print(f"Placing order: {order}")
        queue.enqueue(order) # Place the order in the queue
        time.sleep(0.5) # Delay 0.5 seconds

def serve_order(queue):
    # Start this thread 1 second after place order thread is started.
    time.sleep(1.0)
    while True:
        time.sleep(2.0) # Delay 2 seconds 
        order = queue.dequeue()
        if order is None:
            continue
        print(f"Order served: {order}")
        if queue.is_empty():
            break

# Create a single Queue instance for both functions to use
order_queue = Queue()
orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']

t1 = threading.Thread(target=place_order, args=(order_queue, orders))
t2 = threading.Thread(target=serve_order, args=(order_queue,))

t1.start()
t2.start()

t1.join()
t2.join()

print("All orders have been placed and served.")
