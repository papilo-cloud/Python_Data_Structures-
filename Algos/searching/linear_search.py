
def linear_search(list, search_value):
    for i in range(len(list)):
        if list[i] == search_value:
            return i 
        elif list[i] > search_value:
            break
    return False

print(linear_search([3, 17, 22, 75, 80, 202], 22))