"""
Project Euler Problem 15: Lattice Paths
"""

__author__ = "Benjamin R. Metzger"

import math

#Initial approach, prohibitively slow for larger values
def lattice_paths_recursive(size_x: int, size_y: int) -> int:
    if size_x == 0 and size_y == 0:
        return 1
    
    paths: int = 0
    if size_x > 0:
        paths += lattice_paths_recursive(size_x - 1, size_y)

    if size_y > 0:
        paths += lattice_paths_recursive(size_x, size_y - 1)

    return paths

def lattice_paths(size: int) -> int:
    n: int = size * 2
    return math.factorial(n) // (math.factorial(size) * math.factorial(n - size))

def main():
    print(lattice_paths(20))
    

if __name__ == "__main__":
    main()