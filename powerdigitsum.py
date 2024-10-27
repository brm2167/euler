"""
Project Euler Problem 16: Power Digit Sum
"""

__author__ = "Benjamin R. Metzger"

def power_digit_sum(power: int) -> int:
    seq: str = str(2 ** power)

    sum: int = 0
    for digit in seq:
        sum += int(digit)
    return sum

def main():
    print(power_digit_sum(1000))

if __name__ == "__main__":
    main()