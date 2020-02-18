from sys import stdin


def f(n):
    if not n:
        return 1
    return n * f(n - 1)


N = int(stdin.readline())
L = list(reversed(str(f(N))))
c = 0

for i in L:
    if int(i) == 0:
        c += 1
    else:
        break

print(c)
