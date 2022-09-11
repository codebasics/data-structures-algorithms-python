"""

display

dsearch node

insert
insert_beg
insert_end
insert_at

remove
remove_beg
remove_end
remove_at

try:

delete linkedlist
Nth node from end/beg
count
take a list
print middle
reverse

"""

class node:
    def __init__(self,val=None):
        self.val = val
        self.next = None

class llinkedlist:
    def __init__(self):
        self.head = None
        self.prev = None


ll = llinkedlist()
ll.head = node("first")

#add nodes
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert("x")
ll.insert_end("martell")
ll.insert_at("martell","dorsett")

#remove nodes
ll.remove(5)

#search
ll.search(5)

#delete
ll.remove_beg()
ll.remove_end()
ll.remove_at(2)


#ll.delete_list()
#ll.insert("martell")


#Nth node from end
ll.Nth_node_end(3)

#Nth node from beg
ll.Nth_node_beg(2)

#count
ll.count()

#convert
ll.convert_to_list()

#get middle
ll.middle()

#reverse
ll.reverse()

#display
ll.display()

