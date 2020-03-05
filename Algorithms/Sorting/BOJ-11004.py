from sys import stdin

N, K = map(int, stdin.readline().rstrip().split())
A = sorted(map(int, stdin.readline().rstrip().split()))

print(A[K-1])
