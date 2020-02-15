import sys

lo = 'abcdefghijklmnopqrstuvwxyzabcdefghijklm'
up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM'

S = sys.stdin.readline().replace('\n','')

res = ['' for i in range(101)]

for i in range(len(S)):
    if S[i] in lo:
        idx = lo.find(S[i])
        res[i] = lo[idx+13]
    elif S[i] in up:
        idx = up.find(S[i])
        res[i] = up[idx+13]
    else:
        res[i] = S[i]

print(''.join(res))
    
