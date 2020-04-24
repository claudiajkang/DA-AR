from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
read = lambda: stdin.readline().rstrip()

fibo = [0] * 42
fibo[0] = 1
for i in range(2, 42):
    fibo[i] = fibo[i-1] + fibo[i-2]

T = int(read())
for i in range(T):
    n = int(read())
    print(f"{fibo[n]} {fibo[n+1]}")