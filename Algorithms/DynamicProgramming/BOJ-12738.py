from bisect import bisect_left

input()
A = list(map(int, input().split()))
dp = []

for i in A:
    k = bisect_left(dp, i)
    if len(dp) <= k:
        dp.append(i)
    else:
        dp[k] = i

print(len(dp))
