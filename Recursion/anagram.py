def anagram (word, index = 0):
    if len(word) == index:
        print(''.join(word))
    
    for j in range(index, len(word)):
        
        string = [x for x in word]
        
        temp = string[index]
        string[index] = string[j]
        string[j] = temp
        
        anagram(string, index + 1)
        
(anagram('abc'))