import sys

S = sys.stdin.readline().replace('\n', '')
res = list()
for i in range(len(S)):
    res.append(S[i:])

r = sorted(res)
print('\n'.join(r))
