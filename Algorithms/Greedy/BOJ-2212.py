from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
k = int(read())
arr = list(map(int, read().split()))
arr.sort()

diff = [0] * n
for i in range(n - 1):
    diff[i] = arr[i + 1] - arr[i]

diff.sort(reverse=True)
print(sum(diff[k - 1:]))
