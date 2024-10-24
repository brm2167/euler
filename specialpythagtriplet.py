"""
Project Euler Problem 9: Special Pythagorean Triplet
"""

__author__ = "Benjamin R. Metzger"

import math

def is_natural(num: int | float) -> bool:
    return num >= 0 and math.floor(num) == num

def pythagorean_triplet(target: int) -> int:
    for a in range(1, target // 2 - 1):
        for b in range(a, target // 2):
            c: float = math.sqrt(a ** 2 + b ** 2)
            if is_natural(c) and a + b + c == target:
                return a * b * c

def main():
    print(pythagorean_triplet(1000))

if __name__ == "__main__":
    main()