"""
Project Euler Problem 24: Lexicographic Permutations
"""

__author__ = "Benjamin R. Metzger"

def get_permutations(set: list, permutations: list = [], seq: str = "") -> list:
    if len(set) == 0:
        permutations.append(seq)
        return permutations

    for digit in set:
        new_set: list = set.copy()
        new_set.remove(digit)
        get_permutations(new_set, permutations, seq + str(digit))
    return permutations

def main():
    print(get_permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])[999999])

if __name__ == "__main__":
    main()