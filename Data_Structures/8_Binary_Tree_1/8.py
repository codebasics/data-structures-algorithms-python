# ### Binary Tree Part 1 Exercise

# Add following methods to [BinarySearchTreeNode class](https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/8_Binary_Tree_1/binary_tree_part_1.py) created in main video tutorial

#     1. find_min(): finds minimum element in entire binary tree
#     2. find_max(): finds maximum element in entire binary tree
#     3. calculate_sum(): calcualtes sum of all elements
#     4. post_order_traversal(): performs post order traversal of a binary tree
#     5. pre_order_traversal(): perofrms pre order traversal of a binary tree

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data
        
    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data
        
    def calcluate_sum(self):
        sum = 0
        elements = self.in_order_traversal()
        for i in elements:
            sum += i
        return sum
    
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

numbers_tree = build_tree([15, 12, 7, 14, 27, 20, 23, 88])

print(numbers_tree.find_min())
print(numbers_tree.find_max())
print(numbers_tree.calcluate_sum())
print(numbers_tree.in_order_traversal())
print(numbers_tree.post_order_traversal())
print(numbers_tree.pre_order_traversal())