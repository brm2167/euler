"""
Project Euler Problem 4: Largest Palindrome Product
"""

__author__ = "Benjamin R. Metzger"

def is_palindrome(check: str) -> bool:
    return check == check[::-1]

def palindrome_product(digits: int):
    largest: int = 0
    x_digits: range = range(10 ** digits - 1, 10 ** (digits - 1) - 1, -1)

    for i in x_digits:
        for j in x_digits:
            product: int = i * j
            if product > largest and is_palindrome(str(product)):
                largest = product

    return largest

def main():
    print(palindrome_product(3))

if __name__ == "__main__":
    main()