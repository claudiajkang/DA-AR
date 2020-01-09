class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Node is defined as
    # self.left (the left child of the node)
    # self.right (the right child of the node)
    # self.info (the value of the node)

    def insert(self, val):
        p = self.root
        new_node = Node(val)

        if self.root is None:
            self.root = new_node

        else:
            while True:
                if p.info > val:
                    if p.left is None:
                        p.left = new_node
                        break
                    else:
                        p = p.left

                elif p.info < val:
                    if p.right is None:
                        p.right = new_node
                        break
                    else:
                        p = p.right

# Enter you code here.

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
