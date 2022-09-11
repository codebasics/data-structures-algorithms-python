class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("Vivo"))

    root.add_child(laptop)
    root.add_child(cellphone)

    print("root:",root.data)
    print("laptops parent is -->",laptop.parent.data)

if __name__ == '__main__':
    build_product_tree()
