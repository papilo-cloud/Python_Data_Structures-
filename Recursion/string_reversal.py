def string_reversal(string, index):
    
    if index == 0:
        return string[0]
    return string[index] + string_reversal(string, index - 1)
    
string = 'hello'
print(string_reversal(string, len(string) - 1))