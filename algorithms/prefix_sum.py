arr = [1, 2, 3, 4, 5, 6]

def prefix_sum(list):
    prefix = [0 for i in range(len(list))]
    prefix[0] = list[0]
    for i in range(len(list)):
        prefix[i] = prefix[i - 1] + list[i]
    return prefix

print(prefix_sum(arr))