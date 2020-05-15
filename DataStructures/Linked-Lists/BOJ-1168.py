from sys import stdin

n, k = map(int, stdin.readline().rstrip().split())

if n > 0:
    arr = [i for i in range(1, n+1)]
    print("<", end = "")
    k -= 1
    idx = k
    for i in range(1, n):
        print(arr.pop(idx), end = ", ")
        idx = (idx+k) % len(arr)

    print(arr.pop(idx), end = ">")
