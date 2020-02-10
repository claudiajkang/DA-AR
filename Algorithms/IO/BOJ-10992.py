import sys
  
N = int(sys.stdin.readline())
w = 2*N - 1
ps = ''

if N == 1:
    ps += '*'

else:
    for i in range(N):
        if i == (N-1):
            for k in range(w):
                ps += '*'
        else:
            for j in range(N-i-1):
                ps += ' '
            ps += '*'
            v = 2 * i -1
            for j in range(v):
                ps += ' '
                if j == (v-1):
                    ps += '*'
            ps += '\n'
print(ps)
