# Complete the solve function below.
def solve(s):
    #lst = [word[0].upper() + word[1:] for word in s.split()]
    #s2 = " ".join(lst)
    #return s2 #.title() #.split(' ')[].capitalize()
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = 'hello   world  lol'

    result = solve(s)

    print(result)

    #fptr.close()