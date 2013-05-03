def myfactorial(x):
    n = 1
    if x%1 == 0:        # bad way to test for int; use isinstance(x, (int, long))
        while (x > 0):
            n = n * x
            x = x - 1
        return n
        print n    # printing right after returning will never happen
    else:
        print "Input must be an integer"
