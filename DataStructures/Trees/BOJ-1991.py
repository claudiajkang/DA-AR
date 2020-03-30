from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
tree = {chr(65+i): {'l': None, 'r': None} for i in range(n)}

for i in range(n):
    data, l, r = read().split()

    if l != '.':
        tree[data]['l'] = l

    if r != '.':
        tree[data]['r'] = r


def preOrder(tree, root):
    if root is None:
        return

    print(root, end = "")

    if tree[root]['l'] is None and tree[root]['r'] is None:
        return

    if tree[root]['l'] is not None:
        preOrder(tree, tree[root]['l'])

    if tree[root]['r'] is not None:
        preOrder(tree, tree[root]['r'])

def inOrder(tree, root):
    if root is None:
        return

    if tree[root]['l'] is None and tree[root]['r'] is None:
        if root is not None:
            print(root, end = "")
        return

    if tree[root]['l'] is not None:
        inOrder(tree, tree[root]['l'])

    print(root, end = "")

    if tree[root]['r'] is not None:
        inOrder(tree, tree[root]['r'])


def postOrder(tree, root):
    if root is None:
        return

    if tree[root]['l'] is None and tree[root]['r'] is None:
        if root is not None:
            print(root, end = "")
        return

    if tree[root]['l'] is not None:
        postOrder(tree, tree[root]['l'])

    if tree[root]['r'] is not None:
        postOrder(tree, tree[root]['r'])

    print(root, end = "")

preOrder(tree, 'A')
print()
inOrder(tree, 'A')
print()
postOrder(tree, 'A')