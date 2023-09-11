class TreeNode:
    def __init__(self, data):
        self.data = data
        self.childen = []
        self.parent = None

    def add_child(self, child):
        self.childen.append(child)
        child.parent = self

    def print_tree(self):
        spaces = " " * self.get_level()
        prefix = "|__"
        print(spaces + prefix + self.data)
        if self.childen:
            for i in self.childen:
                i.print_tree()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level


root = TreeNode("Electronics")  # root

phones = TreeNode("Phones")  # child
television = TreeNode("Television")  # child

phones.add_child(TreeNode("iPhones"))
television.add_child(TreeNode("Sony"))

root.add_child(phones)  # adding childen to root
root.add_child(television)  # adding childen to root

root.print_tree()  # printing the tree
