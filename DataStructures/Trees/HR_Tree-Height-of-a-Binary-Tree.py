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


def height(root):
    if root is None:
        return 0
    else:
        if root is not None:
            if root.level is None:
                root.level = 0
            if root.left is not None and root.left.level is None:
                root.left.level = root.level + 1
            if root.right is not None and root.right.level is None:
                root.right.level = root.level + 1

        res_left = height(root.left)
        if res_left <= root.level:
            res_left = root.level
        res_right = height(root.right)
        if res_right <= root.level:
            res_right = root.level

        if res_left >= res_right:
            return res_left

        else:
            return res_right


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))
