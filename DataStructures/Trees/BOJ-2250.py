from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()

def inOrder(num):
    global tree, level, pos

    if tree[num].left: inOrder(tree[num].left)
    tree[num].position = pos
    level[tree[num].level].append(pos)
    pos += 1
    if tree[num].right: inOrder(tree[num].right)


def postOrder(num, level):
    global tree, maxlevel

    if level > maxlevel: maxlevel = level
    tree[num].level = level
    if tree[num].left: postOrder(tree[num].left, level + 1)
    if tree[num].right: postOrder(tree[num].right, level + 1)


class Node:
    def __init__(self):
        self.index = 0
        self.parent = None
        self.level = 0
        self.left = None
        self.right = None
        self.position = -1


n = int(read())
tree = [Node() for i in range(n + 1)]

for i in range(1, n + 1):
    a, b, c = map(int, read().split())
    if b != -1:
        tree[a].left = b
        tree[b].parent = a
    if c != -1:
        tree[a].right = c
        tree[c].parent = a

root = 0

for i in range(1, n + 1):
    if tree[i].parent is None:
        root = i
        break

maxlevel = 0
postOrder(root, 1)
pos = 1
level = [[] for i in range(maxlevel + 1)]
inOrder(root)
res = [0, 0]

for i in range(1, maxlevel + 1):
    if len(level[i]) == 1:
        if 1 > res[1]: res = [i, 1]
    elif len(level[i]) > 1 and (level[i][-1] - level[i][0] + 1) > res[1]:
        res = [i, (level[i][-1] - level[i][0] + 1)]

print(' '.join(map(str, res)))
