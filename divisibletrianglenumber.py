"""
Project Euler Problem 12: Highly Divisible Triangle Number
"""

__author__ = "Benjamin R. Metzger"

import math

def count_divisors(num: int) -> int:
    if num == 1:
        return 1
    
    divisors: int = 2
    for i in range(2, math.floor(math.sqrt(num))):
        if not num % i:
            divisors += 2
    return divisors

def triangle_divisors(target: int) -> int:
    divisors: int = 1
    i: int = 1
    triangle: int = 1
    largest_divisors: int = 0

    while divisors < target:
        i += 1
        triangle += i

        divisors = count_divisors(triangle)
        if divisors > largest_divisors:
            largest_divisors = divisors
            print(divisors)

    return triangle


def main():
    print(triangle_divisors(500))

if __name__ == "__main__":
    main()