from sys import stdin

N, K = map(int, stdin.readline().split())
res = []
PP = [i for i in range(1, N + 1)]
idx = 0

while PP:
    idx = int((idx + K - 1) % len(PP))
    res.append(str(PP.pop(idx)))

print('<' + ', '.join(res) + '>')
