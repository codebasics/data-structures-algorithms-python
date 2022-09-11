class node:
    def __init__(self,val=None):
        self.val = val
        self.next = None

class stack:
    def __init__(self):
    self.size = 1
        self.top = None



t = stack()

t.push("a")
t.push("b")
t.push("c")
t.push("d")
t.pop()
t.pop()
t.pop()
t.pop()
