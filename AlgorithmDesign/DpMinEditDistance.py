def MinEditDistance(s1, s2):
    t = {}
    for i in range(0, len(s1)+1):
        for j in range(0, len(s2)+1):
            if i == 0:
                t[0, j] = j
                continue
            elif j == 0:
                t[i, 0] = i
                continue

            if s1[i-1] == s2[j-1]:
                t[i, j] = t[i-1, j-1]
            else:
                t[i, j] = min(t[i-1, j], t[i-1, j-1], t[i, j-1])+1
    return t[len(s1), len(s2)]


# driver code to test the above code
if __name__ == '__main__':
    str1 = "intention"   # "abcdef"
    str2 = "execution"  # "azced"

    print("The Minimun Edit Distance - Dynamic Programing (Bottom Up) Solution for Strings ('%s' and '%s') is: %s" % (str1, str2, str(MinEditDistance(str1, str2))))