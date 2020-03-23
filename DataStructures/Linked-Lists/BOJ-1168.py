from sys import stdin

n, k = map(int, stdin.readline().rstrip().split())
arr = [i for i in range(1, n+1)]

if n > 0:
    print("<", end = "")
    
    ci = (k-1)
    for i in range(n-1):
        print(arr.pop(ci), end = ", ")
        ci = (ci + k-1) % len(arr)

    print(str(arr.pop()) + ">")
