"""
Project Euler Problem 21: Amicable Numbers
"""

__author__ = "Benjamin R. Metzger"

import math

def sum_divisors(n: int) -> int:
    sum: int = 1
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if not n % i:
            sum += i + (n // i)
    return sum

def main():
    sum: int = 0
    for a in range(10000):
        b: int = sum_divisors(a)
        if b < a or b == a:
            continue
        if sum_divisors(b) == a:
            sum += a + b

    print(sum)

if __name__ == "__main__":
    main()