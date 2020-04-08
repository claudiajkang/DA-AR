from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()

def postOrder(po, io):
    global res
    if len(io) == 0 or len(po) == 0:
        return

    idx = io.index(po[0])
    postOrder(po[1:idx + 1], io[:idx])
    postOrder(po[idx + 1:], io[idx + 1:])
    res.append(po[0])


results = ""
tt = int(read())
for t in range(tt):
    res = []
    n = int(read())
    po = list(map(int, read().split()))
    io = list(map(int, read().split()))
    postOrder(po, io)
    results += ' '.join(map(str, res)) + '\n'

print(results[:-1], end="")
