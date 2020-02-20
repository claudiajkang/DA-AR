from sys import stdin

N, K = map(int, stdin.readline().split())
PP = [i for i in range(1,N+1)]
res = []
idx = 0

while PP:
    idx = (idx + K - 1) % len(PP)
    res.append(str(PP.pop(idx)))

print('<'+', '.join(res)+'>')
