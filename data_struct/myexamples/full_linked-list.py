"""

display

dsearch node

insert
insert_beg
insert_end
insert_at

remove
remove_beg
remove_end
remove_at

try:

delete linkedlist
Nth node from end/beg
count
take a list
print middle
reverse

"""

class node:
    def __init__(self,val=None):
        self.val = val
        self.next = None

class llinkedlist:
    def __init__(self):
        self.head = None
        self.prev = None

    def display(self):
        cur = self.head

        if cur is None:
            print("no linked list")

        while cur:
            print(cur.val,"-->",end="")
            cur = cur.next
        print("None")

    def search(self,trg):
        cur = self.head

        if cur is None:
            print("no linked list")

        found = False
        while cur.next:
            cur = cur.next
            if cur.val == trg:
                found = True
                break
        if found:
            print("found it",cur.val)
        else:
            print("didnt find item")

    def insert(self,val):
        cur = self.head
        new_node = node(val)

        if cur is None:
            cur = new_node

        while cur.next:
            cur = cur.next
        cur.next = new_node

    def insert_end(self,val):
        cur = self.head
        new_node = node(val)

        if cur is None:
            print("no linklist")

        while cur.next:
            cur = cur.next
            if cur.next == None:
                cur.next = new_node
                break

    def insert_at(self,trg,val):# wtf
        cur = self.head
        prev = None
        new_node = node(val)

        found = False
        while cur.next:
            cur = cur.next
            prev = cur
            if cur.next.val == trg:
                found = True
                break
        if found:
            tmp = cur.next
            prev.next = new_node
            new_node.next = tmp
        else:
            print("coukd find that node")

    def remove(self,trg): # 1h:02m
        cur = self.head
        prev = cur

        if cur is None:
            print("no linkedlist")

        found = False
        while cur.next:
            cur = cur.next
            prev = cur
            if cur.next.val == trg:
                found = True
                break
        if found:
                prev.next = cur.next.next
        else:
            print("didnt find it")

    def remove_beg(self):
        cur = self.head

        cur = cur.next
        self.head = cur

    def remove_end(self):
        cur = self.head
        prev = None

        while cur.next:
            prev = cur
            cur = cur.next
            if cur.next == None:
                prev.next = cur.next
                break

    def remove_at(self,trg):
        cur = self.head
        prev = None

        found = False
        while cur.next:
            prev = cur
            cur = cur.next
            if prev.val == trg:
                found = True
                break
        if found:
            prev.next = cur.next
        else:
            print("no found")

    def delete_list(self):
        cur = self.head
        prev = None

        while cur.next:
            cur = cur.next
            prev = cur
            prev.next = None
            print(cur.val)
            if cur.val == None:
                break

    def Nth_node_end(self,n):
        cur = self.head
        cnt = 1
        end = 2
        trg = n #3
        while cur.next:
            cnt += 1
            end += 1
            cur = cur.next
            if end == n:
                break

        print(n,"nodes from end answer:",cur.val)

    def Nth_node_beg(self,n):
        cur = self.head
        cnt = 1
        trg = n
        while cur.next:
            cnt += 1
            cur = cur.next
            if cnt == n:
                break
        print(n,"nodes from begs answer:",cur.val)

    def count(self):
        cur = self.head

        count = 1
        while cur.next:
            count += 1
            cur = cur.next
            if cur.val == None:
                break
        print("count: ",count)

    def convert_to_list(self):
        llist = []
        cur = self.head

        while cur:
            llist.append(cur.val)
            cur = cur.next
        print("convert to list",llist)
    def middle(self):
        cur = self.head
        cnt = 1
        loc = -1
        while cur.next:
            cnt += 1
            loc += 1
            cur = cur.next

            if cur.val == None:
                break
        if (loc == (cnt / 2)):
            print("loc:",loc)
            print("cnt:",cnt)
            print("formula:",loc == (cnt / 2))
            print("odd")
        else:
            print("loc is half of cnt")
            cur = self.head
            count = 1
            print("loc is:",loc)
            while cur.next:
                count += 1
                cur = cur.next
                if count == loc:
                    break
            print("middle is:",cur.val)

    def reverse(self):
        pass

ll = llinkedlist()
ll.head = node("first")

#add nodes
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert("x")
ll.insert_end("martell")
ll.insert_at("martell","dorsett")

#remove nodes
ll.remove(5)

#search
ll.search(5)

#delete
ll.remove_beg()
ll.remove_end()
ll.remove_at(2)


#ll.delete_list()
#ll.insert("martell")


#Nth node from end
ll.Nth_node_end(3)

#Nth node from beg
ll.Nth_node_beg(2)

#count
ll.count()

#convert
ll.convert_to_list()

#get middle
ll.middle()

#reverse
ll.reverse()

#display
ll.display()

