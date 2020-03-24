from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
m = int(read())
broke = read().split()

if n == 100:
    print(0)
    exit()

else:
    channel = []
    res = abs(n-100)

    for i in range(1000001):
        e = True
        for j in str(i):
            if j in broke:
                e = False
                break

        if e:
            if abs(i-n) + len(str(i)) < res:
                res = abs(i-n) + len(str(i))

    print(res)

