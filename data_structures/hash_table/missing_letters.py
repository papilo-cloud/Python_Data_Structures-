def missing_letters(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    hash_table = {}
    
    for index in string:
        hash_table[index] = 1
        
    for letters in alphabet:
        if (hash_table.get(letters) == None):
            print(letters)
    print(string)

string = "the quick brown box jumps over a lazy dog"
missing_letters(string)