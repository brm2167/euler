"""
Project Euler Problem 2: Even Fibonacci Numbers
"""

__author__ = "Benjamin R. Metzger"

def even_fibonacci_sum(end: int) -> int:
    last: int = 2
    second_last: int = 1

    sum: int = 2

    while last + second_last < end:
        following: int = second_last + last
        second_last = last
        last = following
        if last % 2:
            sum += last

    return sum

def main():
    print(even_fibonacci_sum(4000000))

if __name__ == "__main__":
    main()