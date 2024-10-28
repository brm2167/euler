"""
Project Euler Problem 17: Number Letter Counts
"""

__author__ = "Benjamin R. Metzger"

NUMBER_WORDS = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand"
}

def number_word(num: int) -> str:
    keys: list = list(NUMBER_WORDS.keys())
    words: list = []
    last_key: int = len(keys) - 1
    add_and: bool = False

    while num > 0:
        if add_and:
            add_and = False
            words.append("and")

        if num < 100 and num in keys:
            words.append(NUMBER_WORDS[num])
            num = 0
            break

        for i in range(last_key, -1, -1):
            key: int = keys[i]

            if num < key:
                continue

            if key > 99 and not key % 10:
                value: int = int(str(num)[0])
                words.append(NUMBER_WORDS[value])
                num -= key * (value - 1)
                add_and = True

            words.append(NUMBER_WORDS[key])
            num -= key
            last_key = i
            break
    return " ".join(words)

def count_letters(target: str) -> int:
    target = target.upper()

    letters: int = 0
    for char in target:
        ascii: int = ord(char)
        if ascii >= 65 and ascii <= 90:
            letters += 1
    return letters

def main():
    letters: int = 0
    for i in range(1, 1001):
        letters += count_letters(number_word(i))
    print(letters)

if __name__ == "__main__":
    main()