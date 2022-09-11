class node:
    def __init__(self,val=None):
        self.val = val
        self.next = None
        self.prev = None

class linked:
    def __init__(self):
        self.head = None
        self.tail = None

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
