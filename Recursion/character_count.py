def character_count(array, index = 0):
   if len(array) == index:
       return 0
   return len(array[index]) + character_count(array, index + 1)

print(character_count(['ab', 'c', 'def', 'ghij']))