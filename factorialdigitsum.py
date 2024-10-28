"""
Project Euler Problem 20: Factorial Digit Sum
"""

__author__ = "Benjamin R. Metzger"

import math

def digit_sum(n: int) -> int:
    sum: int = 0
    for char in str(n):
        sum += int(char)
    return sum

def main():
    print(digit_sum(math.factorial(100)))

if __name__ == "__main__":
    main()