from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())

if n == 1:
    print(1)

elif n == 2:
    print(min(4, (m + 1) // 2))

elif n >= 3:
    if m <= 6:
        print(min(4, m))

    else:
        print(m-2)