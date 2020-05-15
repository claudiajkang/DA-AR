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

    def add(self, ll):
        data, left, right = ll[0], ll[1], ll[2]
        if not self.root:
            node = Node(data)
            self.root = node

        else:
            node = self.traverse(self.root, data)

        if left != '.': node.left = Node(left)
        if right != '.': node.right = Node(right)

    def traverse(self, node, data):
        if not node: return
        else:
            if node.data == data: return node
            else:
                r = self.traverse(node.left, data)
                if r is not None: return r
                return self.traverse(node.right, data)

    def preOrder(self, node, r):
        if not node: return
        else:
            r.append(node.data)
            t = self.preOrder(node.left, r)
            t = self.preOrder(node.right, r)
            return r

    def inOrder(self, node, r):
        if not node: return
        else:
            t = self.inOrder(node.left, r)
            r.append(node.data)
            t = self.inOrder(node.right, r)
            return r

    def postOrder(self, node, r):
        if not node: return
        else:
            t = self.postOrder(node.left, r)
            t = self.postOrder(node.right, r)
            r.append(node.data)
            return r


n = int(read())
t = Tree()

for i in range(n):
    t.add(read().split())

print(''.join(t.preOrder(t.root, [])))
print(''.join(t.inOrder(t.root, [])))
print(''.join(t.postOrder(t.root, [])))
