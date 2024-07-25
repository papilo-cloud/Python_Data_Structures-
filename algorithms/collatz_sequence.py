def collatz_sequence(num):
    count = 0
    end_count = False
    
    if num == 0:
        return False
    
    while not end_count:
        # print(int(num), end=' ')
        
        if num == 1:
            end_count = True
        if num%2 == 0:
            num /= 2
        else:
            num = (3*num) + 1
            
        count += 1
        
    return count

print(collatz_sequence(35655))