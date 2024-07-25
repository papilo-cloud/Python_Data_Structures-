import stack

def palindrome_checker(word):
    # I imported and used the already build Stack as a module
    lists = stack.Stack()
    reversed_word = ''
    
    for i in word:
        lists.push(i)
    
    while lists.length() > 0:
        reversed_word += lists.pop()
    if reversed_word == word:
        return True
    else:
        return False

print(palindrome_checker('racecar'))
    
    