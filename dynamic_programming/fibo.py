def fibo(n, res):
    if res[n] == 0:
        res[n] = fibo(n-1, res) + fibo(n-2, res)
    return res[n]

n= 10
res = [0] * (n+1)
res[1], res[2] = 1,1
print(fibo(n, res))