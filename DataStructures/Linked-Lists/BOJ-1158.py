from sys import stdin

N, K = map(int, stdin.readline().split())
c = [i for i in range(1, N+1)]
d = []
e = 0

while c:
    e = (e+K-1) % len(c)
    d.append(str(c.pop(e)))

print('<'+', '.join(d)+'>')
