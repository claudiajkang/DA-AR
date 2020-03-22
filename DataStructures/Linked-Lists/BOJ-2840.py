from sys import stdin
read = lambda: stdin.readline().rstrip()

n, k = map(int, read().split())
circle = ['?'] * n

err = False
idx = 0
for _ in range(k):
    mv, val = read().split()
    mv = int(mv)

    idx = (idx+mv) % n

    if (val in circle) and (val != circle[idx]):
        err = True

    elif circle[idx] != '?' and circle[idx] != val:
        err = True

    else:
        circle[idx] = val

if err:
    print('!')

else:
    for i in range(n):
        print(circle[idx-i], end="")
