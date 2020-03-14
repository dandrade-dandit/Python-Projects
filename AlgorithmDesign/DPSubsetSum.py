def SubsetSum(val, w):
    t = {}
    for i in range(0, len(val)):
        for j in range(0, w + 1):
            r=val[i]
            if j < val[i]:
                if j == 0:
                    t[i, j] = True
                    continue

                if i == 0:
                    t[i, j] = False
                else:
                    t[i, j] = t[i - 1, j]
            else:
                if i == 0 and j == val[i]:
                    t[i, j] = True
                    continue
                elif i == 0 and j > val[i]:
                    t[i, j] = False
                    continue
                if t[i-1, j]:
                    t[i, j] = True
                else:
                    t[i, j] = t[i-1, j-val[i]]
    return t[len(val)-1, w]


# driver code to test the above code
if __name__ == '__main__':
    val = [2, 3, 7, 8, 10]
    w = 11
    print("The Subset Sum Problem - Dynamic Programing (Bottom Up) Solution is: %s" % (str(SubsetSum(val, w))))