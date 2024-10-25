"""
Project Euler Problem 14: Longest Collatz Sequence
"""

__author__ = "Benjamin R. Metzger"

def collatz(start: int) -> int:
    num: int = start
    length: int = 1
    while num != 1:
        length += 1
        if num % 2:
            num = 3 * num + 1
        else:
            num /= 2
    return length


def main():
    longest_start: int = 1
    longest: int = 1
    for i in range(2, 1000000):
        length = collatz(i)
        if length > longest:
            longest = length
            longest_start = i
            print(f"New longest: {i} ({length})")
    print(longest_start)

if __name__ == "__main__":
    main()