def addition(n):
    return n + n


numbers = (551, 464, 999, 112)
result = map(addition, numbers)
print(list(result))
