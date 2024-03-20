# 1. In [LinkedList class](https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/3_LinkedList/3_linked_list.py) that we implemented in our tutorial add following two methods,
# ```
# def insert_after_value(self, data_after, data_to_insert):
#     # Search for first occurance of data_after value in linked list
#     # Now insert data_to_insert after data_after node

# def remove_by_value(self, data):
#     # Remove first node that contains data
# ```
# Now make following calls,
# ```
#     ll = LinkedList()
#     ll.insert_values(["banana","mango","grapes","orange"])
#     ll.print()
#     ll.insert_after_value("mango","apple") # insert apple after mango
#     ll.print()
#     ll.remove_by_value("orange") # remove orange from linked list
#     ll.print()
#     ll.remove_by_value("figs")
#     ll.print()
#     ll.remove_by_value("banana")
#     ll.remove_by_value("mango")
#     ll.remove_by_value("apple")
#     ll.remove_by_value("grapes")
#     ll.print()
# ```

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

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
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
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
            

            

# ll = LinkedList()
# ll.insert_values(["banana","mango","grapes","orange"])
# ll.insert_at(1,"blueberry")
# ll.remove_at(2)
# ll.print()
# ll.insert_values([45,7,12,567,99])
# ll.insert_at_end(67)
# ll.print()
                
ll = LinkedList()
ll.insert_values(["banana","mango","grapes","orange"])
ll.print()
ll.insert_after_value("mango","apple") # insert apple after mango
ll.print()
ll.remove_by_value("orange") # remove orange from linked list
ll.print()
ll.remove_by_value("figs")
ll.print()
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.print()
ll.remove_by_value("apple")
ll.remove_by_value("grapes")
ll.print()