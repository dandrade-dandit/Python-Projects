def fractionalKnapsack(wt, val, w):
    val_wt = dict((k, val[k] / wt[k]) for k in range(0, len(wt)))
    r = 0

    for key, value in sorted(val_wt.items(), key=lambda item: item[1], reverse=True):
        if w >= wt[key]:
            r += val[key]
            w -= wt[key]
        else:
            r += w * value
            w -= w
            break
        ## print("%s: %s" % (key, value))

    return r


# driver code to test the above code
if __name__ == '__main__':
    val = [5, 10, 15, 7, 8, 9, 4, 20]
    wt = [1, 3, 5, 4, 1, 3, 2, 6]
    #val_wt = [5, 3.3, 3, 1.75, 8, 3, 2, 3.33]
    #index = [0, 1, 2, 3, 4, 5, 6, 7]

    w = 15
    print("The result of the Divide and Conquer - Fractional Knapsack problem is: " + str(fractionalKnapsack(wt, val, w)))
