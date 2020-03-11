from sys import stdin
read = lambda: int(stdin.readline().rstrip())

t = read()
testcase = [read() for _ in range(t)]
mn = max(testcase)
dp = [0] * (mn+1)

tc = 0
for i in range(1, mn+1):
    if i in [1,2,3]:
        dp[i] = 1
    elif i in [4, 5]:
        dp[i] = 2
    elif i in [6,7,8]:
        if i == 6:
            tc = 3
        dp[i] = dp[i-tc] + dp[i-1]
        tc += 1
    else:
        dp[i] = dp[i-5] + dp[i-1]
        tc += 1

for i in testcase:
    print(dp[i])
