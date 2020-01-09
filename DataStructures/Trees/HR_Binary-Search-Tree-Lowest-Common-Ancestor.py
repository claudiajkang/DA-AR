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


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''


def lca(root, v1, v2):
    current = root
    pstack = list()

    while True:
        if current is not None:
            if current.info is root.info:
                current.level = 0

            if current.left and current.left.level is None:
                current.left.level = current.level + 1

            if current.right and current.right.level is None:
                current.right.level = current.level + 1

            pstack.append(current)
            current = current.left

        elif pstack:
            current = pstack.pop()
            current = current.right

        else:
            break

    v1stack = list()
    v2stack = list()

    current = root

    while True:
        if current is not None:
            v1stack.append(current)

            if v1 is current.info:
                break

            if v1 < current.info:
                current = current.left

            else:
                current = current.right

    current = root
    while True:
        if current is not None:
            v2stack.append(current)

            if v2 is current.info:
                break

            if v2 < current.info:
                current = current.left

            else:
                current = current.right

    tv1 = v1stack.pop()
    tv2 = v2stack.pop()

    while True:
        if tv1.level is tv2.level:
            if tv1.info is tv2.info:
                break
            else:
                tv1 = v1stack.pop()
                tv2 = v2stack.pop()

        elif tv1.level > tv2.level:
            tv1 = v1stack.pop()

        else:
            tv2 = v2stack.pop()

    return tv1

# Enter your code here


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print(ans.info)
