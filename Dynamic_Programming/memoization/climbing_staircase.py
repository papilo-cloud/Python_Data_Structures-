def clinbing_staircase(path, memo = {}):
    if path == 0:
        return 1
    if path < 0:
        return 0
    if not memo.get(path):
        memo[path] = clinbing_staircase(path - 1, memo) + clinbing_staircase(path - 2, memo)  
    return memo[path]
    
print(clinbing_staircase(10))