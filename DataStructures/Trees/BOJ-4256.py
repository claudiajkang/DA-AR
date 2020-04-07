from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

read = lambda: stdin.readline().rstrip()


def postOrder(preorder, inorder):
    N = len(inorder)
    if len(preorder) == 0: return
    root = preorder[0]
    l = inorder.index(root)
    postOrder(preorder[1:l + 1], inorder[0:l])
    postOrder(preorder[l + 1:N], inorder[l + 1:N])
    print(root, end=" ")


T = int(read())
for i in range(T):
    N = int(read())

    preorder = list(map(int, read().split()))
    inorder = list(map(int, read().split()))
    postOrder(preorder, inorder)
    print()
