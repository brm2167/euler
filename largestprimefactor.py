"""
Project Euler Problem 3: Largest Prime Factor
"""

__author__ = "Benjamin R. Metzger"

import math

def is_prime(num: int) -> bool:
    for i in range(2, math.ceil(math.sqrt(num)) + 1):
        if not num % i:
            return False

    return True

def largest_prime_factor(product: int) -> int:
    for i in range(math.ceil(math.sqrt(product)), 0, -1):
        if (not product % i) and is_prime(i):
            return i

def main():
    print(largest_prime_factor(600851475143))

if __name__ == "__main__":
    main()