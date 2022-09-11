class bst:
    def __init__(self,val=None):
        self.val = val
        self.l = None
        self.r = None

    def insert(self,val):
        nd = bst(val)
        if val < self.val:
            if self.l == None:
                self.l = nd
            else:
                self.l.insert(val)
        else:
            if self.r == None:
                self.r = nd
            else:
                self.r.insert(val)

    def postorder(self):
        if self.l:
            self.l.postorder()
        if self.r:
            self.r.postorder()
        print(self.val)

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

print("##################")

tree[1].insert(40)
tree[1].insert(60)
print()
print("displaying 2d tree")
