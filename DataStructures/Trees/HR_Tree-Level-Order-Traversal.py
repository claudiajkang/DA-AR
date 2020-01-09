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


def levelOrder(root):
    current = root
    tstack = list()
    llist = dict()

    while True:
        if current is not None:
            if current.info is root.info:
                current.level = 0

            if current.left and current.left.level is None:
                current.left.level = current.level + 1

            if current.right and current.right.level is None:
                current.right.level = current.level + 1

            if current.level not in llist.keys():
                llist[current.level] = list()

            if current.info not in llist[current.level]:
                llist[current.level].append(current)

            tstack.append(current)
            current = current.left

        elif tstack:
            current = tstack.pop()
            current = current.right
        else:
            break

    klist = sorted(llist.keys())

    for i in klist:
        for j in llist[i]:
            print(j.info, end=' ')

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)