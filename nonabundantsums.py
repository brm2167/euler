"""
Project Euler Problem 23: Non-Abundant Sums
"""

__author__ = "Benjamin R. Metzger"

import math

def is_abundant(n: int) -> bool:
    if n == 1:
        return False

    sum: int = 1
    max: int = math.ceil(math.sqrt(n))
    for i in range(2, max):
        if not n % i:
            sum += i + (n // i)
    if max ** 2 == n:
        sum += max
        
    return sum > n

def abundantly_summable(n: int) -> bool:
    for i in range(1, math.ceil(n / 2) + 1):
        if is_abundant(i) and is_abundant(n - i):
            return True
    return False

def main():
    sum: int = 0
    for i in range(1, 28124):
        if not abundantly_summable(i):
            sum += i
    print(sum)

if __name__ == "__main__":
    main()