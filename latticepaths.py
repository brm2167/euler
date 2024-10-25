"""
Project Euler Problem 15: Lattice Paths
"""

__author__ = "Benjamin R. Metzger"

def lattice_paths(size_x: int, size_y: int) -> int:
    if size_x == 0 and size_y == 0:
        return 0
    
    paths: int = 1
    for x in range(size_x - 1, 0, -1):
        paths += lattice_paths(x, size_y)

    for y in range(size_y - 1, 0, -1):
        paths += lattice_paths(size_x, y)

    return paths

def main():
    print(lattice_paths(2, 2))
    

if __name__ == "__main__":
    main()