from sys import stdin

N = stdin.readline().rstrip()

if '0' not in N:
    print(-1)

else:
    sum_digit = 0
    for i in N:
        sum_digit += int(i)

    if sum_digit % 3 != 0:
        print(-1)
    else:
        for i in sorted(N, reverse=True):
            print(i, end='')