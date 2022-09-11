class node:
    def __init__(self,val=None):
        self.val = val
        self.l = None
        self.r = None

class bst:
    def __init__(self):
        self.head = None

    def lvl_order(self):
        """"
        level order queue:
            1.)give q the starting pos
            2.)as long as the q is full

            3.) take first thing in q mark as visited
            4.) check if that popped items has children
                if they do put then in the queue

        """"
        vis = []
        q = []
        q.append(self.head)

        while len(q) > 0:
            cur = q.pop(0)
            vis.append(cur)

            if cur.l:
                q.append(cur.l)
            if cur.r:
                q.append(cur.r)

        for x in vis:
            print(x.val)

t = bst()
t.head = node(4)
t.head.l = node(2)
t.head.r = node(8)
t.head.l.l =  node(1)
t.head.l.r = node(3)
t.head.r.l = node(5)
t.head.r.r =  node(10)
t.lvl_order()


