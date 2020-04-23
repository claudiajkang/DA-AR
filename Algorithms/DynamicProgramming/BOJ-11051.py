from math import factorial
from sys import stdin

n, k = map(int, stdin.readline().rstrip().split())
result = factorial(n) // (factorial(k) * factorial(n - k))
print(result % 10007)
