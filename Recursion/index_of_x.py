def index_of_x(string, index = 0):
    
    if index == len(string):
        return
    if string[index] == 'x':
        return index
    
    return index_of_x(string, index + 1)
    
string = 'abcdefghijklmnopqrstuvwyzx'
print(index_of_x(string))
