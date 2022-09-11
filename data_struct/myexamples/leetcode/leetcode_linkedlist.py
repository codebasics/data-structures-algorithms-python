class node:
    def __init__(self,val=None):
        self.val = val
        self.next = None

class llinkedlist:
    def __init__(self):
        self.head = None
        self.prev = None

    def display(lst):
        if lst is None:
            print("no linked list")

        for i in range(len(mynodes)):
            print(lst[i].val,"-->",end="")
            i += 1
        print("None")

    def insert_list(self,mynodes):
        print("the list")
        print(mynodes)
        cur = self.head
        lst = []
        for x in mynodes:
            new_nd = node(x)

            lst.append(new_nd)
        return llinkedlist.display(lst)


ll = llinkedlist()

mynodes = [1,2,3,4,5]

ll.insert_list(mynodes)
