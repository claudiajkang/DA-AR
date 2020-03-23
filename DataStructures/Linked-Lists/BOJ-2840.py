from sys import stdin
read = lambda: stdin.readline().rstrip()

n, k = map(int, read().split())
circle = ['?'] * n

ci = 0
err = False
for i in range(k):
    c, v = read().split()
    ci = (ci-int(c)) % n

    if circle[ci] == '?':
        if v in circle:
            err = True
            break
        else:
            circle[ci] = v

    elif circle[ci] == v:
        continue

    elif circle[ci] != '?':
        err = True
        break

if err:
    print('!')

else:
    circle = circle[ci:] + circle[:ci]
    for i in range(n):
        print(circle[i], end = "")
