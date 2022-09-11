class node:
    def __init__(self,val):
        self.val = val
        self.next = None

class linked:
    def __init__(self):
        self.q = [ ]
        self.head = None

l = linked()

arr = [1,2,3]

l.list_link(arr)
l.insert("x")
l.display()
