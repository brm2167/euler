"""
Project Euler Problem 11: Largest Product in a Grid
"""

__author__ = "Benjamin R. Metzger"

def largest_product_grid(length: int, grid: list) -> int:
    largest_product: int = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            #Left to right
            if j < len(grid) - length + 1:
                product: int = 1

                for k in range(j, j + length):
                    product *= grid[i][k]

                if product > largest_product:
                    largest_product = product

def main():
    with open("problem11grid.txt") as file:
        grid: list = []
        for line in file:
            row: list = line.strip().split()
            for i in range(len(row)):
                row[i] = int(row[i])
            grid.append(row)
    print(largest_product_grid(4, grid))

if __name__ == "__main__":
    main()