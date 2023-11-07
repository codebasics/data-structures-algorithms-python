class node:
    def __init__(self,val=None):
        self.val = val
        self.next = None

class stack:
    def __init__(self):
        self.size = 1
        self.top = None


    def peek(self):
        cur = self

        if cur.top is None:
            print("nothing in stack")
        else:
            print(cur.top.val)

    def push(self,val):
        cur = self
        new_nd = node(val)

        if cur.top is None:
            cur.top = new_nd
        else:
            cur.size += 1
            new_nd.next = cur.top
            cur.top = new_nd
        print(self.size)

    def pop(self):
        cur = self

        if cur.size == 0:
            print("stack empty")
        else:
            tmp = cur.top.val
            cur.top = cur.top.next
            cur.size -= 1
            cur = cur.top
            if cur is None:
                print("empty")
            else:
                print("next top -> {} popped top --> {}" \
                  .format(cur.val,tmp))

t = stack()

t.push("a")
t.push("b")
t.push("c")
t.push("d")
t.pop()
t.pop()
t.pop()
t.pop()
