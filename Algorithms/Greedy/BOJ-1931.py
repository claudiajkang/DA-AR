from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
time = []

for i in range(n):
    time.append(list(map(int, read().split())))

time.sort(key=lambda x: x[0])
time.sort(key=lambda x: x[1])

count = 0
temp = 0

for i in range(n):
    if time[i][0] >= temp:
        temp = time[i][1]
        count += 1

print(count)
