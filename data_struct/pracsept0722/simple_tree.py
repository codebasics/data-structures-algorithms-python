class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    pass
if __name__ == '__main__':
    build_product_tree()
