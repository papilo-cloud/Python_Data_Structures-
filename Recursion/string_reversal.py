
string = 'hello'

# Botton-Up approach
def string_reversal(string, index):
    
    if index == 0:
        return string[0]
    return string[index] + string_reversal(string, index - 1)
    

# Top-Down approach
def reversal(string):
    if len(string) == 1:
        return string[0]
    return reversal(string[1:]) + string[0]