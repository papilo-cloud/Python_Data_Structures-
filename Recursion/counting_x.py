string = 'xhexlxlxo'

# Botton-Up approach
def count_x(string, index = 0):
    if index == len(string):
        return 0
        
    if string[index] == 'x':
        return 1 + count_x(string, index + 1)
    else:
        return count_x(string, index + 1)


# Top-Down approach
def count_x_2(string):
    if not string:
        return 0
    if string[0] == 'x':
        return 1 + count_x_2(string[1:])
    else:
        return 1 + count_x_2(string[1:])