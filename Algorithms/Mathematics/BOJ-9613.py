from sys import stdin

def gcd(a, b):
    if b:
        return gcd(b, a%b)
    return a

N = int(stdin.readline())

for i in range(N):
    t = list(map(int, stdin.readline().strip().split()))
    c = t.pop(0)
    res = 0
    for a in range(c):
        for b in range(a+1, c):
            res += gcd(t[a],t[b])

    print(res)
