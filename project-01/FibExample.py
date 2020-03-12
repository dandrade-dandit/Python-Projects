
import datetime
memo = {}
fibd = {}

def fib (n):
    if n <= 2: f = 1
    else: f = fib(n - 1) + fib(n - 2)
    return f

def fib2 (n):
    if n in memo: return memo[n]
    if n <= 2: f = 1
    else: f = fib2(n - 1) + fib2(n - 2)
    memo[n] = f
    return f

def fib3 (n):
    for k in range(1,n+1):
        if k <= 2: f = 1
        else: f = fibd[k - 1] + fibd[k - 2]
        fibd[k] = f
    return fibd[n]

a = datetime.datetime.now()
result_fib = fib(40)
b = datetime.datetime.now()
print (result_fib)
print(b-a)

a = datetime.datetime.now()
result_fib = fib2(40)
b = datetime.datetime.now()
print (result_fib)
print(b-a)

a = datetime.datetime.now()
result_fib = fib3(40)
b = datetime.datetime.now()
print (result_fib)
print(b-a)