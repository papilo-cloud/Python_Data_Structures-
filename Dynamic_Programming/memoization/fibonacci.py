def fibonacci(num, memo = {}):
    if num == 0 or num == 1:
        return num
    
    if not memo.get(num):
        memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo)
    return memo[num]
print(fibonacci(7))