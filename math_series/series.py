def fibonacci(n):
    """
    This function should contain only one parameter, n, and should return the fibonacci series' nth value.  
    """

    if n==0 or n==1 : 
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):  
    """
   The lucas function should return the nth value in the lucas numbers collection.

    """

    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, one=0, two=1): 
    """
    The sum_series function accepts one necessary argument (n) and two optional arguments (one) and (two), respectively, to calculate the sum of the series.
    template's one and two parameters
    Fibonacci Sequence

    """

    if n==0:
        return one
    elif n==1:
        return two
    else:
        return sum_series(n-1, one=one, two=two) + sum_series(n-2, one=one, two=two)