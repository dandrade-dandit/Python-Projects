import time;
def fibnaive (n):
    if n == 1 or n == 2: return 1;
    else: return fibnaive(n-1) + fibnaive(n-2);

memo={};
def fibdptopdown (n):
    if n in memo: return memo[n];
    if n == 1 or n == 2: result = 1;
    else: result = fibdptopdown(n-1) + fibdptopdown(n-2);
    memo[n] = result;
    return result;


def fibdpbottomup (n):
    fib = {};
    for k in range(1, n+1):
        if k <= 2: f=1;
        else: f = fib[k-1]+fib[k-2];
        fib[k]=f;
    return fib[n]

# driver code to test the above code
if __name__ == '__main__':
    n=37
    start_time = time.time()
    result = fibnaive(n)
    elapsed_time = time.time() - start_time
    mlsec = repr(elapsed_time).split('.')[1][:5]
    printexectime = time.strftime("%H:%M:%S.{} %Z".format(mlsec), time.gmtime(elapsed_time))
    print("The Result of Fibonacci of " + str(n) + " - Naive Version: " + str(result) + " was executed in " + str(printexectime) + ".");

    start_time = time.time()
    result = fibdptopdown(n)
    elapsed_time = time.time() - start_time
    mlsec = repr(elapsed_time).split('.')[1][:3]
    printexectime = time.strftime("%H:%M:%S.{} %Z".format(mlsec), time.gmtime(elapsed_time))
    print("The Result of Fibonacci of " + str(n) + " - DP TopDown Version: " + str(result) + " was executed in " + str(printexectime) + ".");

    start_time = time.time()
    result = fibdpbottomup(n)
    elapsed_time = time.time() - start_time
    mlsec = repr(elapsed_time).split('.')[1][:3]
    printexectime = time.strftime("%H:%M:%S.{} %Z".format(mlsec), time.gmtime(elapsed_time))
    print("The Result of Fibonacci of " + str(n) + " - DP BottomUp Version: " + str(result) + " was executed in " + str(printexectime) + ".");