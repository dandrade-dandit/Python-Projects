import random

def power(x, y, p):
    res = 1

    x = x % p
    while y > 0:

        if y & 1:
            res = (res * x) % p

        y = y >> 1  # y = y/2
        x = (x * x) % p

    return res


def miillerTest(d, n):
    a = 2 + random.randint(1, n - 4)

    x = power(a, d, n)

    if x == 1 or x == n - 1:
        # Return inconclusive
        return True

    while d != n - 1:
        x = (x * x) % n
        d *= 2

        if x == 1:
            # Return composite
            return False
        if x == n - 1:
            # Return inconclusive
            return True

    # Return composite
    return False


def isPrime(n, k):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    d = n - 1
    while d % 2 == 0:
        d //= 2

    # Iterate given nber of 'k' times
    for i in range(k):
        if miillerTest(d, n) == False:
            return False

    return True


# Driver Code
# Number of iterations
k = 4;

print("All primes smaller than 1000: ");
for n in range(2000, 2050):
    if (isPrime(n, k)):
        print(n, end=" ");

