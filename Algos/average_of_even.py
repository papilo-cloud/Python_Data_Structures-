def average_of_even_nembers(list):
    sum = 0
    count_of_even_numbers = 0
     
    for index in list:
        if index%2 == 0:
            sum += index
            count_of_even_numbers += 1
    return (sum / count_of_even_numbers)
    

print(average_of_even_nembers([1,2,3,4,6,8,7]))

# time complexity O(N)