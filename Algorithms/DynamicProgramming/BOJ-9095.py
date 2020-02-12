import sys

T = int(sys.stdin.readline())
inputs = list()

for i in range(T):
    inputs.append(int(sys.stdin.readline()))

m = max(inputs)
dp = [0 for i in range(m+1)]
 
for i in range(1, m+1):
    if 1<= i <= 3:
        dp[i] = [1, 2, 4][i-1]
    else:
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for j in inputs:
    print(dp[j])
