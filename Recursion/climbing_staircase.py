# Let’s say we have a staircase of N steps, and a person has the ability to climb
# one, two, or three steps at a time. How many different possible “paths” can
# someone take to reach the top? Write a function that will calculate this for N
# steps

def num_of_path(path):
    if path < 0: 
        return 0
    if path == 0 or path == 1:
        return 1
    return num_of_path(path - 1) + num_of_path(path - 2)  + num_of_path(path - 3)

print(num_of_path(3))