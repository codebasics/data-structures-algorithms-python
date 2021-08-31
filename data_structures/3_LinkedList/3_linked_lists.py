class Node:
    def __init__(self,val=None,next=None):
        self.val = val 
        self.next = next


class LinkedList:
    def __init__(self):
        self.head=None
    
    def show(self):
        if self.head == None:
            print('Linked List is empty')
            return
        else:
            itr = self.head
            while itr:
                print(itr.val,' --> ',end='')
                itr=itr.next 
            print('None')
    
    def getlength(self):
        itr = self.head
        c=0
        while itr:
            c+=1
            itr = itr.next
        return c
    
    def insert_at_end(self,val):
        if self.head is  None:
            node = Node(val,None)  
            self.head = node 
            return
        else:
            itr = self.head
            while itr.next :
                itr=itr.next
            itr.next=Node(val,None)
    
    def insert_at_beginning(self,val):
        node = Node(val,self.head)
        self.head=node 

    def insert_values(self,x):
        self.head = None
        for d in x:
            self.insert_at_end(d)
    
    def insert_at_pos(self,pos,val):
        if pos < 0 or pos >= self.getlength():
            raise Exception("Invalid syntax")

        if pos == 0:
            self.insert_at_beginning(val)
            return 
        elif pos == self.getlength() - 1:
            self.insert_at_end(val)
            return
        else:
            itr = self.head
            c = 0
            while itr:
                if c==pos -1:
                    node = Node(val,itr.next)
                    itr.next=node 
                    break
                c+=1
                itr = itr.next

    def remove_at_pos(self,pos):
        if pos < 0 or pos >= self.getlength():
            raise Exception('Invalid position')
        if pos ==0:
            self.head=self.head.next
            return
        itr = self.head
        c=0
        while itr:
            if c==pos-1:
                itr.next=itr.next.next
                break
            c+=1
            itr=itr.next
        pass
    # Adding for task
    def insert_after_value(self,val_before,val):
        if self.head is None:
            return

        if self.head.val==val_before:
            self.head.next = Node(val,self.head.next)
            return

        itr=self.head
        c=0
        while itr:
            if val_before==itr.val:
                self.insert_at_pos(c+1,val)
                break
            c+=1
            itr=itr.next
        else:
            print('Data is not in the linked list')

    def remove_by_val(self,val):
        if self.head is None:
            return

        if self.head.val == val:
            self.head = self.head.next
            return

        itr=self.head
        c=0
        while itr:
            if itr.val == val:
                self.remove_at_pos(c)
                break
            itr=itr.next
            c+=1
        else:
            print('No such value present in linked list')
            

    
if __name__ == '__main__':
    '''
    l=LinkedList()
    l.insert_values(['A','B','C','D'])
    l.show()
    l.insert_at_pos(2,'F')
    l.show()
    l.remove_at_pos(3)
    l.show()
    l.insert_at_end('R')
    l.show()
    l.insert_at_beginning('J')
    l.show()
    l.insert_after_value('A','K')
    l.show()
    l.remove_by_val('K')
    l.show()
    '''
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.show()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.show()
    ll.remove_by_val("orange") # remove orange from linked list
    ll.show()
    ll.remove_by_val("figs")
    ll.show()
    ll.remove_by_val("banana")
    ll.remove_by_val("mango")
    ll.remove_by_val("apple")
    ll.remove_by_val("grapes")
    ll.show()
