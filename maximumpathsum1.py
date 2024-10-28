"""
Project Euler Problem 18: Maximum Path Sum I
"""

__author__ = "Benjamin R. Metzger"

def max_path_sum(triangle: list, index: int = 0) -> int:
    if len(triangle) == 0:
        return 0
    
    path_1: int = triangle[0][index] + max_path_sum(triangle[1:], index)
    path_2: int = triangle[0][index] + max_path_sum(triangle[1:], index + 1)

    if path_1 > path_2:
        return path_1
    return path_2

def main():
    triangle: list = []
    with open("problem18triangle.txt") as triangle_file:
        for line in triangle_file:
            row: list = line.strip().split()
            for i in range(len(row)):
                row[i] = int(row[i])
            triangle.append(row)
    print(max_path_sum(triangle))
    

if __name__ == "__main__":
    main()