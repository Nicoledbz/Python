from unicodedata import name


numbers = [4, 6, 2, 7, 1]
numbers.sort()
print(numbers)

names = ["Carlos", "Ray", "Alex", "Kelly"]
print(names)
print(sorted(names))
print(names)

print(sorted(name, key=len))