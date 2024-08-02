def combinations(string, n):
    if n == 1:
        return string
    return [digit + bit for digit in combinations(string, 1)
            for bit in combinations(string, n - 1)]

print(combinations('abc', 3))