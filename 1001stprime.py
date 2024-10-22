"""
Project Euler Problem 7: 10,000st prime
"""

__author__ = "Benjamin R. Metzger"

import math

def is_prime(num: int) -> bool:
    for i in range(2, math.ceil(math.sqrt(num)) + 1):
        if not num % i:
            return False

    return True

def nth_prime(n: int) -> int:
    primes: int = 1
    i: int = 2
    while primes < n:
        i += 1
        if is_prime(i):
            primes += 1

    return i

def main():
    print(nth_prime(10001))

if __name__ == "__main__":
    main()