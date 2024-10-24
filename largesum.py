"""
Project Euler Problem 13: Large Sum
"""

__author__ = "Benjamin R. Metzger"

def main():
    with open("problem13nums.txt") as file:
        sum: int = 0
        for line in file:
            sum += int(line.strip())
        print(str(sum)[:10])
    

if __name__ == "__main__":
    main()