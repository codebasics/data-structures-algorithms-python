# #### Data structures exercise: General Tree

# 1. Below is the management hierarchy of a company.

#     ![ss](management_both.PNG)

# Extent [tree class](https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/7_Tree/7_tree.py) built in our
# main tutorial so that it takes **name** and **designation** in data part of TreeNode class.
# Now extend print_tree function such that it can print either name tree, designation tree or name and designation tree. As shown below,

#    ![](all_trees.png)

# Here is how your main function should will look like,
# ```
# if __name__ == '__main__':
#     root_node = build_management_tree()
#     root_node.print_tree("name") # prints only name hierarchy
#     root_node.print_tree("designation") # prints only designation hierarchy
#     root_node.print_tree("both") # prints both (name and designation) hierarchy

#potentially delete the "data" field in the constructor

class TreeNode:
    def __init__(self, data, name, designation):
        self.data = data
        self.children = []
        self.parent = None
        self.name = name
        self.designation = designation

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, type):
        if type == 'both':
            value = self.name + f" ({self.designation})"
            
        elif type == 'designation':
            value = self.designation
        
        else:
            value = self.name

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + value)

        if self.children:
            for child in self.children:
                child.print_tree(type)
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_management_tree():
    root = TreeNode("","Nilpul","CEO")

    cto = TreeNode("","Chinmay","CTO")

    infra_head = TreeNode("","Vishwa","Infrastructure Head")

    infra_head.add_child(TreeNode("","Dhaval","Cloud Manager"))
    infra_head.add_child(TreeNode("","Abhijit","App Manager"))

    cto.add_child(infra_head)

    cto.add_child(TreeNode("","Aamir","Application Head"))

    hr_head = TreeNode("","Gels","HR Head")

    hr_head.add_child(TreeNode("","Peter","Recruitment Manager"))
    hr_head.add_child(TreeNode("","Waqas","Policy Manager"))

    root.add_child(cto)
    root.add_child(hr_head)

    return root

root_node = build_management_tree()

root_node.print_tree('both')
root_node.print_tree('designation')
root_node.print_tree('name')