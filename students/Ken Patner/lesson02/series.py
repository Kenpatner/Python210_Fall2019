
def fibonacci(n):
    '''Function, called to the nth element.  Begins with a list with 0 and 1.'''
    '''The sum of the 2 most recent elements is calculated up to element n, and adds itself to the end of the list'''
    print ("Fibonacci Series called to element", n)
    fib = [0,1]
    for i in range(n):
        fib.append(fib[-1] + fib[-2])
    print (fib)
print (fibonacci(15))


def lucas(n):
    '''Function, called to the nth element.  Begins with a list with 2 and 1.'''
    '''The sum of the 2 most recent elements is calculated up to element n, and adds itself to the end of the list'''
    print ("Lucas Series called to element", n)
    lucas = [2,1]
    for i in range(n):
        lucas.append(lucas[-1] + lucas[-2])
    print (lucas)
print (lucas(15))


def sum_series(n, n0=0, n1=1):
    print (
        "Fibonacci series called to element", n, "if the first two elements are not specified.  \nIf they are,", n0,"is the first element and", n1,"is the second element, still called to element", n)
    if n0 == 0 and n1 == 1:
        fib_series = [n0, n1]
        for i in range (n):
            fib_series.append(fib_series[-1] + fib_series[-2])
        return print(fib_series)
    else:
        other_series = [n0, n1]
        for i in range (n):        
            other_series.append(other_series[-1] + other_series[-2])
        return print(other_series)
sum_series(10, 4, 9)
