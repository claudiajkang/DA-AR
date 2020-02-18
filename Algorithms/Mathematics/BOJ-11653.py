from sys import stdin
  
N = int(stdin.readline())
res = []
i = 2

while N != 1:
    if N % i > 0:
        i += 1
        continue

    R = N % i
    N = N // i
    if R:
        i += 1
    else:
        res.append(str(i))

print('\n'.join(res))
