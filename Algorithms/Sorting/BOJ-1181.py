from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
arr = set()

for i in range(n):
    l = read()
    arr.add(l)

arr = list(arr)
arr.sort()
arr.sort(key=lambda x: len(x))

print("\n".join(arr))
