def factor(n):
    '''
    Prints a string with all the factors of a (n) number.
    n: an integer to be factored
    Expected output:
    >>> n = 15
    >>> '1 3 5 15'
    '''
    factors = ''
    for i in range(1, round(n / 2) + 1):
        if n % i == 0:
            factors += f'{i} '
    factors += f'{n}'
    print(factors)

factor(int(input('Please enter an integer: ')))
