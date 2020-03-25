from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())

for i in range(n):
    temp = 0
    point = 0
    for j in read():
        if j == "X":
            temp = 0
        elif j == "O":
            temp += 1
        point += temp

    print(point)