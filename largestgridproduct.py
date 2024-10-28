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

            #Up-down
            if i < len(grid) - length + 1:
                product: int = 1

                for k in range(i, i + length):
                    product *= grid[k][j]

                if product > largest_product:
                    largest_product = product

            #Up-right diagonal
            if i + 1 >= length and j < len(grid) - length + 1:
                product: int = 1

                for k in range(length):
                    product *= grid[i - k][j + k]

                if product > largest_product:
                    largest_product = product

            #Down-right diagonal
            if i < len(grid) - length + 1 and j < len(grid) - length + 1:
                product: int = 1

                for k in range(length):
                    product *= grid[i + k][j + k]

                if product > largest_product:
                    largest_product = product

    return largest_product

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