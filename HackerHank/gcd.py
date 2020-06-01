def gcd_euclidean(a, b):
    if a > b:
        swap(a, b)

    r = a % b

    while r != 0:
        a = b
        b = r
        r = a % b

    return b


def swap(a, b):
    t = b
    b = a
    a = t


if __name__ == '__main__':
    a = 310 #1160718174
    b = 710 #316258250
    g = gcd_euclidean(a, b)
    print(f'GCD({a}, {b}) = {g}')