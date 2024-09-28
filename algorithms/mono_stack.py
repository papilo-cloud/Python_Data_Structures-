def mono_stack(arr):
    n = len(arr)
    nge = [-1]*n
    stk = []
    for i in range(n-1, -1, -1):
        while stk and stk[-1] <= arr[i]:
            stk.pop()
        
        if i < n and stk:
            nge[i] = stk[-1]
        stk.append(arr[i])
            
            
    return nge, stk

x = [2,1,2,5,4]
print(mono_stack(x))