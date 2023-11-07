class node:
    def __init__(self,val=None):
        self.val = val
        self.n = None

class queuend:
    def __init__(self):
        self.fr = None
        self.r = None
        self.count = 0

    def get_inl(self,val):
        frt = self.fr
        r = self.r
        nd = node(val)

        if frt is None:
            #frt = nd
            r = nd
        while r.n:
            nd.n = frt 
        print(r.val)
        print("front",frt.val)


    def get_otl(self):
        frt = self.fr
        r = self.r


myq = queuend()

myq.get_inl(1)
myq.get_inl(3)
myq.get_inl(5)
myq.get_inl(6)
myq.get_inl(8)
myq.get_otl()

"""
same things as node-stack

but for this one

top will be head
and tail will be the last


head -- 1
3
5
6
tail -- 8

every new node.next will be tail

"""
