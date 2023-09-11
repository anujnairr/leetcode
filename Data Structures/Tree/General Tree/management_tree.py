class TreeNode:
    def __init__(self, data, position) -> None:
        self.data = data
        self.position = position
        self.childen = []
        self.parent = None

    def add_child(self, child):
        self.childen.append(child)
        child.parent = self

    def print_the_organisation(self, action="both"):
        prefix = "|__"
        spaces = " " * self.get_level() * 2
        print_statement = ""
        if action == "both":
            print_statement = spaces + prefix + \
                self.data + " (" + self.position + ")"
        elif action == "name":
            print_statement = spaces + prefix + self.data
        elif action == "designation":
            print_statement = spaces + prefix + self.position

        print(print_statement)

        for child in self.childen:
            child.print_the_organisation(action)

    def print_until_level(self, level):
        prefix = "|__"
        spaces = " " * self.get_level()
        # print(spaces + prefix + self.data)
        if self.get_level() > level:
            return
        else:
            print(spaces + prefix + self.data)
            for child in self.childen:
                child.print_until_level(level)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level


ceo = TreeNode("Nilupul", "CEO")
cto = TreeNode("Chinmay", "CTO")
hr = TreeNode("Gels", "HR Head")

ceo.add_child(cto)
ceo.add_child(hr)

ifra_lead = TreeNode("Vishwa", "Infra Lead")
app_lead = TreeNode("Amir", "Application Head")

cto.add_child(ifra_lead)
cto.add_child(app_lead)

ifra_lead.add_child(TreeNode("Dhaval", "Cloud Manager"))
ifra_lead.add_child(TreeNode("Abhijit", "App Manager"))

hr.add_child(TreeNode("Peter", "Recruitment Manager"))
hr.add_child(TreeNode("Waqas", "Policy Manager"))

# ceo.print_the_organisation()
# ceo.print_the_organisation("both")

ceo.print_until_level(2)
