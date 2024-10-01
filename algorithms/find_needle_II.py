def ans(haystack, needle):
    try:
        return haystack.index(needle)
    except ValueError:
        return -1
    
haystack = "leetcode"
needle = "code"

print(ans(haystack, needle))
