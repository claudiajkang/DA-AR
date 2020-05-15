from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()


def preOrder(num):
    global tree, res
    if tree[num].child == []:
        res += 1
    else:
        for cur in tree[num].child:
            if tree[cur]:
                preOrder(cur)

class Node:
    def __init__(self):
        self.child = []

    def add(self, child):
        self.child.append(child)

    def remove(self, child):
        self.child.remove(child)


n = int(read())
tree = [Node() for i in range(n + 1)]
temp = list(map(int, read().split()))
deleteNode = int(read())
root = 0

for i in range(n):
    if temp[i] == -1:
        root = i
        continue
    tree[temp[i]].add(i)

if temp[deleteNode] == -1:
    print(0)

else:
    tree[temp[deleteNode]].remove(deleteNode)
    res = 0
    preOrder(root)
    print(res)
