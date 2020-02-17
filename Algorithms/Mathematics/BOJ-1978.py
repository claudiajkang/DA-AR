from sys import stdin


def get_un():
    un = [i for i in range(1001)]
    for i in range(2, 1001):
        if un:
            m = int(1000 / i)
            for j in range(2, m + 1):
                un[i * j] = 0

    un = sorted(un)
    idx = un.index(1)
    return un[idx + 1:]


u = get_un()
N = int(stdin.readline())
t = list(map(int, stdin.readline().strip().split()))
res = 0

for i in t:
    if i in u:
        res += 1

print(res)