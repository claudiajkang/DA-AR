from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()


def postOrder(po, io):
    global res
    if not io: return

    iroot = io.index(po[0])
    postOrder(po[1:iroot + 1], io[0:iroot])
    postOrder(po[iroot + 1:], io[iroot + 1:])
    res.append(po[0])


result = ""
tt = int(read())
for t in range(tt):
    n = int(read())
    res = []
    preorder = list(map(int, read().split()))
    inorder = list(map(int, read().split()))
    postOrder(preorder, inorder)
    result += ' '.join(map(str, res)) + '\n'

print(result[:-1], end="")
