from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

read = lambda: stdin.readline().rstrip()


def inOrder(num):
    global tree, idx, levels

    if tree[num]['left']: inOrder(tree[num]['left'])
    idx += 1
    tree[num]['pos'] = idx
    levels[tree[num]['level']].append(idx)
    if tree[num]['right']: inOrder(tree[num]['right'])


def preOrder(num, level):
    global tree, maxlevel

    if level > maxlevel: maxlevel = level
    tree[num]['level'] = level
    if tree[num]['left']: preOrder(tree[num]['left'], level + 1)
    if tree[num]['right']: preOrder(tree[num]['right'], level + 1)


n = int(read())
tree = {i: {'parent': None, 'level': 0, 'left': None, 'right': None, 'pos': 0} for i in range(1, n + 1)}
idx = 0
maxlevel = 0
root = 0

for i in range(1, n + 1):
    d, l, r = map(int, read().split())
    if l != -1:
        tree[d]['left'] = l
        tree[tree[d]['left']]['parent'] = d
    if r != -1:
        tree[d]['right'] = r
        tree[tree[d]['right']]['parent'] = d

for i in range(1, n + 1):
    if tree[i]['parent'] is None:
        root = i
        break

preOrder(root, 1)
levels = [[] for i in range(maxlevel + 1)]
inOrder(root)
res = [0, 0]

for i in range(1, maxlevel + 1):
    if (len(levels[i]) == 1) and (1 > res[1]):
        res = [i, 1]
    elif (len(levels[i]) >= 1) and (levels[i][-1] - levels[i][0]) + 1 > res[1]:
        res = [i, levels[i][-1] - levels[i][0] + 1]

print(' '.join(map(str, res)))
