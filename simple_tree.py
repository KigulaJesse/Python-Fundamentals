class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def display(self, level=0):
        print(" " * level + str(self.value))
        for child in self.children:
            child.display(level+1)

    def search(self,value):
        
        if value == self.value:
            status = "found"
            return status
        print("Outside for Loop:",self.value)
        # print(self.children)
        for child in self.children:
            print("In for Loop:",child.value)
            status = child.search(value)
            if status:
                return status

        return None
        
root = TreeNode("A")

childB = TreeNode("B")
root.add_child(childB)

childC = TreeNode("C")
root.add_child(childC)

childD = TreeNode("D")
childB.add_child(childD)

childE = TreeNode("E")
childB.add_child(childE)

childF = TreeNode("F")
childC.add_child(childF)

childG = TreeNode("G")
childC.add_child(childG)


# root.display(2)

search_node = "E"
status = root.search(search_node)

if status == "found":
    print("We found E")
else:
    print("E has disappeared")