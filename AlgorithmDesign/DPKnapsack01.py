def Knapsack01(wt, val, w):
    t = {}
    for i in range(0, len(wt)):
        for j in range(0, w + 1):
            r=wt[i]
            if j < wt[i]:
                if i == 0 or j == 0:
                    t[i, j] = 0
                    continue
                t[i, j] = t[i-1, j]
            else:
                if i == 0:
                    t[i, j] = val[i]
                    continue
                t[i, j] = max(val[i]+t[i - 1, j-wt[i]], t[i-1, j])
    return t[len(wt)-1, w]


# driver code to test the above code
if __name__ == '__main__':
    wt = [5, 6, 8, 4, 7, 2, 2]
    val = [50, 50, 64, 46, 50, 45, 30]
    w = 19;
    print("The 0/1 Kanpsack Problem - Dynamic Programing (Bottom Up) Solution is: %s" % (str(Knapsack01(wt, val, w))))