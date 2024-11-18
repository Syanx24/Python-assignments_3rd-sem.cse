import math


def is_prime(n):
    for i in range(2,int(n**(0.5)+1)):
        if n%i ==0:
            return False
        return True


def is_palindrome(n):
    st = n[::-1]
    if st == n:
        return True
    else:
        return False