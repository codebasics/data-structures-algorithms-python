class node:
    def __init__(self,val=None):
        self.val = val
        self.next = None
        self.prev = None

class linked:
    def __init__(self):
        self.head = None

l = linked()

l.head = node("start")
l.insert("a")


print("test")
print(l.head.val)
print(l.head.next.val)
print(l.head.next.next.val)
