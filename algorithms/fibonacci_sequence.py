def fibonacci(num):
    previous_fib = 0
    current_fib = 1
    index = 0
    
    while index <= num:
        print(previous_fib, end=' ')
        current_fib = current_fib + previous_fib
        previous_fib = current_fib - previous_fib
        index += 1

fibonacci(8)