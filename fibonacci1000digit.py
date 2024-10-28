"""
Project Euler Problem 25: 1000-digit Fibonacci Number
"""

__author__ = "Benjamin R. Metzger"

def x_digit_fibonacci(digits: int) -> int:
    last: int = 2
    second_last: int = 1
    i: int = 3

    while last < 10 ** (digits - 1):
        following: int = second_last + last
        second_last = last
        last = following
        i += 1

    return i

def main():
    print(x_digit_fibonacci(1000))

if __name__ == "__main__":
    main()