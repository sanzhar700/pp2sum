from functools import reduce

numbers = [5, 2, 8, 1, 4]

# len()
print(len(numbers))

# sum()
print(sum(numbers))

# min()
print(min(numbers))

# max()
print(max(numbers))

# sorted()
print(sorted(numbers))

# map()
result = list(map(lambda x: x * 2, numbers))
print(result)

# filter()
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)

# reduce()
result = reduce(lambda x, y: x + y, numbers)
print(result)

# enumerate()
fruits = ["Apple", "Banana", "Orange"]

for i, fruit in enumerate(fruits):
    print(i, fruit)

# zip()
scores = [90, 85, 100]

for fruit, score in zip(fruits, scores):
    print(fruit, score)

# Type checking
x = 10
print(type(x))
print(isinstance(x, int))

# Type conversions
a = "25"

print(int(a))
print(float(a))
print(str(100))