class node:
    def __init__(self,val=None):
        self.val = val
        self.next = None

class linked:
    def __init__(self):
        self.q = [ ]
        self.head = None

    def list_link(self,lst):
        cur = self.head

        if cur is None:
            cur = node(lst[0])
            self.q.insert(0,cur)

        for i in range(1,len(lst)):
            nd = node(lst[i])
            self.q.append(nd)

    def display(self):
        cur = self.q
        ev,od = [],[]
        for i in range(len(self.q)):
            if i % 2:
                ev.append(( cur[i].val,"-->"))
        for i in range(len(self.q)):
            if i % 1:
                od.append(( cur[i].val,"-->"))

        print("even",ev)
        print("odd",od)


l = linked()

arr = []
for i in range(1,35,3):
    arr.append(i)

l.list_link(arr)
print("the head ",l.q[0].val)
l.display()
