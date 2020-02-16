import sys

N = sys.stdin.readline().strip()
TN = int(N, base=2)
print(str(oct(TN))[2:])
