# 2. Implement doubly linked list. The only difference with regular linked list is that double linked has prev node reference as well. That way you can iterate in forward and backward direction.
# Your node class will look this this,
# ```
# class Node:
#     def __init__(self, data=None, next=None, prev=None):
#         self.data = data
#         self.next = next
#         self.prev = prev
# ```
# Add following new methods,
# ```
# def print_forward(self):
#     # This method prints list in forward direction. Use node.next

# def print_backward(self):
#     # Print linked list in reverse direction. Use node.prev for this.
# ```
# Implement all other methods in [regular linked list class]
#(https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/3_LinkedList/3_linked_list.py) 
# and make necessary changes for doubly linked list (you need to populate node.prev in all those methods)

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        # When you find the end of the list, create a new node with data.
        # Set the new node's 'next' to None (it's the end of the list) and 'prev' to itr (the current last node).
        new_node = Node(data, None, itr)
        itr.next = new_node

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def print_forward(self): # This method prints list in forward direction. Use node.next
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    
    def print_backward(self): # Print linked list in reverse direction. Use node.prev for this.
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        ## after this runs, we are at the end of the linked list
        
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.prev else str(itr.data)
            itr = itr.prev
        print(llstr)
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(data, self.head,None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node  
            self.head = node 

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next,itr.prev)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            self.head.prev - None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):

        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return
        
        itr = self.head #the itr is the first value in the Linked List

        while itr.next:
            if itr.data == data_after: # Search for first occurance of data_after value in linked list
                # Now insert data_to_insert after data_after node
                node2 = Node(data_to_insert,itr.next) 
                itr.next = node2
                return
            itr = itr.next

        raise Exception("the data you're searching for doesn't exist")
        ## if it doesn't find the value after going through the whole list, raise Exception
    
    def remove_by_value(self, data):
        # Handle the case where the list is empty
        if self.head is None:
            print("The list is empty.")
            return
        
        # Handle the case where the node to be removed is the head
        if self.head.data == data:
            self.head = self.head.next
            return
        
        itr = self.head #the itr is the first value in the Linked List
        prev = None

        while itr:
            if itr.data == data: #if we find the data
                prev.next = itr.next # Remove first node that contains data
            prev = itr
            itr = itr.next

dll = DoublyLinkedList()
dll.insert_values(["banana","mango","grapes","orange"])
dll.print_forward()
dll.print_backward()
dll.insert_after_value("mango","apple") # insert apple after mango
dll.print_forward()
dll.remove_by_value("orange") # remove orange from linked list
dll.print_forward()