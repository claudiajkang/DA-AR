from sys import stdin
read = lambda: stdin.readline().rstrip()

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, data, left, right):
        if not self.root:
            node = Node(data)
            self.root = node

        else:
            node = self.traverse(self.root, data)

        if left != '.':
            node.left = Node(left)

        if right != '.':
            node.right = Node(right)

    def traverse(self, node, data):
        if node:
            if data == node.data: return node
            else:
                l = self.traverse(node.left, data)
                if l: return l
                return self.traverse(node.right, data)

        else:
            return

    def preOrder(self, node):
        if node is None: return
        print(node.data, end = "")

        self.preOrder(node.left)
        self.preOrder(node.right)

    def inOrder(self, node):
        if node is None: return
        self.inOrder(node.left)
        print(node.data, end = "")
        self.inOrder(node.right)

    def postOrder(self, node):
        if node is None: return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.data, end = "")

N = int(read())
t = Tree()
for i in range(N):
    v, l, r = read().split()
    t.add(v, l, r)

t.preOrder(t.root)
print()
t.inOrder(t.root)
print()
t.postOrder(t.root)