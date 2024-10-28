"""
Project Euler Problem 10: Summation of Primes
"""

__author__ = "Benjamin R. Metzger"

import math

def is_prime(num: int) -> bool:
    for i in range(2, math.ceil(math.sqrt(num)) + 1):
        if not num % i:
            return False

    return True

def prime_summation(maximum: int) -> int:
    sum: int = 2
    for i in range(3, maximum, 2):
        if is_prime(i):
            sum += i
    return sum

def main():
    print(prime_summation(2000000))

if __name__ == "__main__":
    main()