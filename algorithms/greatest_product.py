def greatest_products(array):
    
    return array[len(array) - 1] * array[len(array) - 2] * array[len(array) - 3]
    # prod = 1
    # steps = 0
    # for i in range(len(array) - 2):
    #     temp = array[i] * array[i + 1] * array[i + 2]
    #     steps += 1
    #     if temp > prod:
    #         prod = temp
    #     temp = 0 
    # print(steps)
    # return prod
print(greatest_products([4,2,3,4,1]))