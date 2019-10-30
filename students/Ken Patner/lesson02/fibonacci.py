def fibonacci(n):
    """a series of numbers calculated to the nth argument given, where 
    the next integer is determined by the by adding the sum of the previous two.
    Start with a list where the first two entries are 0 and 1.  Begin a for loop through
    the nth argument that appends onto the list the sum of the last two indicies in the list."""

    fib = [0,1]
    for i in range(n):
        fib.append(fib[-1]+fib[-2])
    print (fib)
print (fibonacci(15))