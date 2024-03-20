# 2. Build below location tree using **TreeNode** class

#     ![](location_trees.png)

# Now modify print_tree method to take tree level as input. And that should print tree only upto that level as shown below,

#    ![](location_trees_all.png)

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level
    
    # original code
    # def print_tree(self):
    #     spaces = ' ' * self.get_level() * 3
    #     prefix = spaces + "|__" if self.parent else ""
    #     print(prefix + self.data)
    #     if self.children:
    #         for child in self.children:
    #             child.print_tree()
    
    def print_tree(self,level):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                if child.get_level() <= level:
                    child.print_tree(level)

    # def print_tree(self, level):
    #     for i in range(level):
    #         spaces = ' ' * self.get_level() * 3
    #         prefix = spaces + "|__" if self.parent else ""
    #         print(prefix + self.data)
    #         if self.children:
    #             for child in self.children:
    #                 child.print_tree(level)

    # def print_tree(self, level):
    #     spaces = ' ' * self.get_level() * 3
    #     prefix = spaces + "|__" if self.parent else ""
    #     print(prefix + self.data)
    #     if self.children:
    #         for i in range(level):
    #             self.children[i].print_tree(i)
        

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_country_tree():
    globe = TreeNode("Global")

    india = TreeNode("India")
    gujarat = TreeNode("Gujarat")
    karnataka = TreeNode("Karnataka")

    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNode("USA")
    new_jersey = TreeNode("New Jersey")
    california = TreeNode("California")

    new_jersey.add_child(TreeNode("Princeton"))
    new_jersey.add_child(TreeNode("Trenton"))

    california.add_child(TreeNode("San Fransisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))

    usa.add_child(new_jersey)
    usa.add_child(california)

    globe.add_child(india)
    globe.add_child(usa)

    return globe

root_node = build_country_tree()

root_node.print_tree(3)