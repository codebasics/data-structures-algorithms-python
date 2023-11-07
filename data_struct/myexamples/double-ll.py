class node:
    def __init__(self,val=None):
        self.val = val
        self.next = None
        self.prev = None

class linked:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self,val):
        cur = self.head
        tail = self.head
        nd = node(val)

        if cur is None:
             cur = nd

        while cur.next:
            cur = cur.next
        cur.next = nd
        nd.prev = cur

    def display_next(self):
        cur = self.head
        while cur :
            print(cur.val,"-->",end="")
            cur = cur.next
        print("None")

    def display_prev(self):
        cur = self.head
        while cur :
            print(cur.val,"<--",end="")
            cur = cur.next
        print("None")

l = linked()
l.head = node("a")
l.insert("b")
l.insert("c")
l.insert("d")
l.insert("e")
l.insert("f")
l.insert("g")
l.display_next()
l.display_prev()
