def LCS(s1, s2):
    t = {}
    for i in range(0, len(s1)+1):
        for j in range(0, len(s2)+1):
            if i == 0 or j == 0:
                t[i, j] = 0
                continue
            if s1[i-1] == s2[j-1]:
                t[i, j] = t[i-1, j-1]+1
            else:
                t[i, j] = max(t[i-1, j], t[i, j-1])
    return t[len(s1), len(s2)]


# driver code to test the above code
if __name__ == '__main__':
    str1 = "abcb"   # "abcdef"
    str2 = "abdcab"  # "azced"
    print("The Longest Common Subsequence(LCS) - Dynamic Programing (Bottom Up) Solution for Strings ('%s' and '%s') is: %s" % (str1, str2, str(LCS(str1, str2))))