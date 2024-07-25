# This problem is known as the “Unique Paths” problem: Let’s say you have
# a grid of rows and columns. Write a function that accepts a number of rows
# and a number of columns, and calculates the number of possible “shortest”
# paths from the upper-leftmost square to the lower-rightmost square.
def unique_path(rows, columns):
    if rows == 1 or columns == 1:
        return 1
    return unique_path(rows, columns - 1) + unique_path(rows - 1, columns)

print(unique_path(3, 6))