numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [x if x % 2 != 0 else x**2 for x in numbers]
print(result)