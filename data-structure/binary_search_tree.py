class Node:
    def __init__(self, value=None, level=1):
        self.value = value
        self.level = level
        self.left = None
        self.right = None

    def add_next_node(self, value, level_here=2):
        new_node = Node(value, level_here)

        if not self.value:
            self.value = new_node

        elif not self.left :
            self.left = new_node

        elif not self.right :
            self.right = new_node

        else:
            self.left = self.left.add_next_node(value, level_here+1)

        return self


class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self.root.add_next_node(value)

BT = BinaryTree()

for i in range(0,10):
    BT.add_node(i)


