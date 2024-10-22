"""
Project Euler Problem 6: Sum Square Difference
"""

__author__ = "Benjamin R. Metzger"

def sum_square(end: int) -> int:
    sum: int = 0
    for i in range(1, end + 1):
        sum += i ** 2
    return sum

def square_sum(end: int) -> int:
    sum: int = 0
    for i in range(1, end + 1):
        sum += i
    return sum ** 2

def main():
    print(square_sum(100) - sum_square(100))

if __name__ == "__main__":
    main()