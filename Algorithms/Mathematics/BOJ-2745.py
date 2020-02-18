from sys import stdin

N, B = stdin.readline().strip().split()
B = int(B)
print(int(N, base=B))