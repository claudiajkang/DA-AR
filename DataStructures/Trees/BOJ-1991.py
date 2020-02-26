from sys import stdin


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None

    def preorder(self, node):
        print(node, end='')
        if not node.left == None: self.preorder(node.left)
        if not node.right == None: self.preorder(node.right)

    def inorder(self, node):
        if not node.left == None: self.inorder(node.left)
        print(node, end='')
        if not node.right == None: self.inorder(node.right)

    def postorder(self, node):
        if not node.left == None: self.postorder(node.left)
        if not node.right == None: self.postorder(node.right)
        print(node, end='')

    def traverse(self, node, v, lst):
        if node:
            if v != node.data:
                self.traverse(node.left, v, lst)
                self.traverse(node.right, v, lst)
            else:
                lst.append(node)

    def add(self, val, left_node, right_node):
        if self.root is None:
            node = Node(val)
            self.root = node
        else:
            lst = []
            self.traverse(self.root, val, lst)
            node = lst[0]

        if left_node != '.':
            node.left = Node(left_node)

        if right_node != '.':
            node.right = Node(right_node)


N = int(input())
t = Tree()
for i in range(N):
    v, l, r = input().split()
    t.add(v, l, r)

t.preorder(t.root)
print()
t.inorder(t.root)
print()
t.postorder(t.root)
