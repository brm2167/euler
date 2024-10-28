"""
Project Euler Problem 22: Names Scores
"""

__author__ = "Benjamin R. Metzger"

import csv

def ascii_score(name: int) -> int:
    score: int = 0
    for char in name:
        score += ord(char) - 64
    return score

def main():
    with open("problem22names.csv") as names_file:
        csv_reader = csv.reader(names_file)
        names: list = next(csv_reader)
        names.sort()

        score: int = 0
        for i in range(len(names)):
            name: str = names[i]
            score += ascii_score(name) * (i + 1)

    print(score)
            
        

if __name__ == "__main__":
    main()