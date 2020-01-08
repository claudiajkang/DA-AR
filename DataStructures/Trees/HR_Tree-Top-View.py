class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def topView(root):
    current = root
    stack = list()
    res = dict()

    while True:
        if current is not None:
            if current.info is root.info:
                current.level = 0
                current.hr = 0
            if current.left and current.left.level is None:
                current.left.level = current.level + 1
                current.left.hr = current.hr - 1
            if current.right and current.right.level is None:
                current.right.level = current.level + 1
                current.right.hr = current.hr + 1

            if current.hr not in res.keys():
                res[current.hr] = [current.level, current.info]
            if current.hr in res.keys():
                v = res[current.hr]
                if v[0] > current.level:
                    res[current.hr] = [current.level, current.info]

            stack.append(current)
            current = current.left

        elif (stack):
            current = stack.pop()
            current = current.right

        else:
            break

    sorted_index = sorted(res.keys())
    for i in sorted_index:
        print(res[i][1], end=' ')


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)