""" Assignment factorial_n
    Created on 27-10-2020,  11:59
    @author Alejo Cain """
def sum_proper_divisors(n):
    result = 0
    for i in range(1, n):
        if n % i == 0:
            result += i

    return result

def is_perfect(n):
    return sum_proper_divisors(n) == n

print(is_perfect(28))