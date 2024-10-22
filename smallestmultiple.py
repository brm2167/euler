"""
Project Euler Problem 5: Smallest Multiple
"""

__author__ = "Benjamin R. Metzger"

def smallest_multiple(product: int) -> int:
    i: int = product + 1
    found: bool = False

    while not found:
        found = True
        for j in range(product, 0, -1):
            if i % j:
                found = False
                i += 1
                break
    return i


def main():
    print(smallest_multiple(20))

if __name__ == "__main__":
    main()