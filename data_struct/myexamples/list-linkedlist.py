class node:
    def __init__(self,val):
        self.val = val
        self.next = None

class linked:
    def __init__(self):
        self.q = [ ]
        self.head = None

    def list_link(self,lst): #list to linkedlsit
        for i in range(0, len(lst)):
            nd = node(lst[i])
            self.q.append(nd)

    def insert(self,val): #value to node
        self.q.append( node(val) )

    def display(self): #print the q of nodes
        for i in range(0,len(self.q)):
            print(self.q[i].val,"-->",end="")
        print("None")

    def peek_head(self):
        print(self.head.val)
l = linked()

arr = [1,2,3]

l.list_link(arr)
l.insert("x")
l.display()
