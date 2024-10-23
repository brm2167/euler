"""
Project Euler Problem 9: Special Pythagorean Triplet
"""

__author__ = "Benjamin R. Metzger"

import math

def is_natural(num: int | float) -> bool:
    return num >= 0 and num == math.floor(num)

def pythagorean_triplet(target: int) -> int:
    maximum: int = math.floor(math.sqrt(target))
    for a in range(maximum - 1):
        for b in range(a, maximum):
            c = 0 #pass

def main():
    pass

if __name__ == "__main__":
    main()