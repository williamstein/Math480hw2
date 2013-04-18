def myfactorial(x):
    n = 1
    if x%1 == 0:
        while (x > 0):
            n = n * x
            x = x - 1
        return n
        print n
    else:
        print "Input must be an integer"
