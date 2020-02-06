import sys

N = sys.stdin.readline()
q = int(len(N)/10)
idx = 10

for i in range(q+1):
    v = N[idx-10:idx]
    if v == '':
        break
    print(v)
    idx += 10
