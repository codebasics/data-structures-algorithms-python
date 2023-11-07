class bst:
    def __init__(self,val=None):
        self.val = val
        self.l = None
        self.r = None


    def inorder(self):

        if self.l:
            self.l.postorder()
        print(self.val)
        if self.r:
            self.r.postorder()

    def postorder(self):

        print(self.val)
        if self.l:
            self.l.postorder()
        if self.r:
            self.r.postorder()

    def insert(self,val):

        if val < self.val:
            if self.l == None:
                self.l = bst(val)
            else:
                self.l.insert(val)
        else:
            if self.r == None:
                self.r = bst(val)
            else:
                self.r.insert(val)

    def prt2d(self,sp,h):
        #dis between lv
        sp += h

        cur = self

        if cur is None:
            return

        bst.prt2d(cur.r,sp,h)
        print()
        for i in range(h,sp):
            print(" ",end="")
        print(cur.val,end="")
        print()
        bst.prt2d(cur.l,sp,h)

tree = [bst(50),bst(50)]

tree[0].insert(20)
tree[0].insert(16)
tree[0].insert(10)
tree[0].insert(18)
tree[0].insert(60)
tree[0].insert(70)
tree[0].insert(65)
tree[0].insert(100)

tree[0].postorder()
print()
print("displaying 2d tree")
tree[0].prt2d(0,5)

print("##################")

tree[1].insert(40)
tree[1].insert(60)
tree[1].inorder()
print()
print("displaying 2d tree")
tree[1].prt2d(0,5)
