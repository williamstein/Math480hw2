Math480hw2
========

Homework 2

"""
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
"""

I created a simple factorial algorithm called myfactorial that takes in any integer. 
It first creates an n varible equal to 1. Then it goes into an if statement to test
whether the input varible is an integer. If x is an integer, the code goes through a 
while loop only while the input x is greater than 0. If x is greater than 0, the code
multiplies n by x to get a new n value and decreases the value of x by 1. The while 
loop continues until x is equal to 0. After the while loop finishes, the code returns
the value n and prints it as well. If x is not an integer, the code simple prints 
"Input must be an integer". 

myfactorial(3) = 6
myfactorial(3.1) = Input must be an integer
