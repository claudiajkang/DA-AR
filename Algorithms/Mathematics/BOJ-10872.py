from sys import stdin
  
def f(n):
    if n == 0:
        return 1
    return n * f(n-1)

N = int(stdin.readline())
print(f(N))
