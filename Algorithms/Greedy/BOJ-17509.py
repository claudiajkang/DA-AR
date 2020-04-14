from sys import stdin

arr = [[] for i in range(11)]
sum = 0

for i in range(11):
    arr[i] = list(map(int, stdin.readline().rstrip().split()))

arr.sort(key=lambda x: x[0])
time = 0

for idx in range(11):
    time += arr[idx][0]
    sum += (time + 20 * arr[idx][1])

print(sum)