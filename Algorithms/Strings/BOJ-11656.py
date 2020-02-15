from sys import stdin

S = stdin.readline().replace('\n','')
res = list()

for i in range(len(S)):
        res.append(S[i:])

print('\n'.join(sorted(res)))
