def activitySelectionProblem(a, s, f):
    i = 0
    r = a[i] + ":[s:" + str(s[i]) + " -> f:" + str(f[i]) + "] "
    for j in range(1, len(f)):
        if (s[j] >= f[i]):
            r += a[j] + ":[s:" + str(s[j]) + " -> f:" + str(f[j]) + "] "
            i = j
    return r

# driver code to test the above code
if __name__ == '__main__':
    a = ["A1", "A2", "A3", "A4", "A5", "A6"]   # Activities  // Ordered like that (A3, A2, A1, A5, A4, A6).
    s = [0, 3, 1, 5, 5, 8]                     # Start Time  // Ordered like that ( 1,  3,  0,  5,  5,  8).
    f = [6, 4, 2, 9, 7, 9]                     # Finish Time // Ordered like that ( 2,  4,  6,  7,  9,  9).
    f, s, a = zip(*sorted(zip(f, s, a)))       # Sort 3 lists(arrays) based on Finish Time (array f).
    print("Following activities are selected : " + activitySelectionProblem(a, s, f))
