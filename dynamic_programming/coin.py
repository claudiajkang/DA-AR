def solve(n, coins):
    if n == 0 or n < 0:
        return 0
    else:
        val = 0
        best = None
        for i in coins:
            if i <= n:
                val = val + solve(n-i, coins) + 1
                best = min(best, val)

        if best is None:
            return 0

        return best

def min(a,b):
    if a is None:
        return b
    elif a>b:
        return b
    return a

n = 6
coins = {1,3,4}
r = solve(n, coins)
print(r)