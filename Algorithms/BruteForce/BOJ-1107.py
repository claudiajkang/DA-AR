from sys import stdin
read = lambda: stdin.readline().rstrip()

enabled = {str(x) for x in range(10)}
N = int(read())
M = int(read())

disabled = set(read().split())
enabled -= disabled

res = abs(N - 100)

for i in range(1000001):
    is_true = True
    for pn in str(i):
        if pn not in enabled:
            is_true = False
            break
    if is_true is True:
        res = min(res, abs(N - i) + len(str(i)))

print(res)
