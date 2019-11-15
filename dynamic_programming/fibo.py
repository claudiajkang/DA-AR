def fibo(n, res):
    if n == 1 or n == 2:
        if res[n] == 0:
            res[n] = 1
        return 1
    elif res[n] == 0:
        res[n] = fibo(n-1, res) + fibo(n-2, res)

    return res[n]

n = 100
res = [0] * (n+1)
print(fibo(n,res))