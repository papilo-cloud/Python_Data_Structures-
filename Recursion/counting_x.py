def count_x(string, index = 0):
    if index == len(string):
        return 0
        
    if string[index] == 'x':
        return 1 + count_x(string, index + 1)
    else:
        return count_x(string, index + 1)
print(count_x('xhexlxlxo'))