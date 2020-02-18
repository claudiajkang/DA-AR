from sys import stdin

N, B = map(int, stdin.readline().strip().split())
res = ''

while N > 0:
    N, R = divmod(N, B)
    if R > 9:
        res = chr(55+R) + res
        continue
    res = str(R) + res

print(res)
