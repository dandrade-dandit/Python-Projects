def fib (n):
    seq = [1, 1]
    for i in range(2, n):
        seq.append(i)
        seq[i] = seq[i-1] + seq[i-2]
    return seq
    # return [n-1]

result_fib = fib(30)
print (result_fib)