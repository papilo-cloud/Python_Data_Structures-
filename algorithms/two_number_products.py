def two_number_products(list):
    products = []
    
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            products.append(list[i] * list[j])
            
    return products

print(two_number_products([1,2,3,4,5]))

# time complexity is O(N^2 / 2) ~ O(N^2)