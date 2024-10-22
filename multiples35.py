"""
Project Euler Problem 1: Multiples of 3 or 5
"""

__author__ = "Benjamin R. Metzger"

def get_sum(end: int) -> int:
    sum: int = 0
    for i in range(3, end):
        if not i % 3 or not i % 5:
            sum += i
    return sum

def main():
    print(get_sum(1000))

if __name__ == "__main__":
    main()