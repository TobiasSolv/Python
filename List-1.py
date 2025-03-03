fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print("\n")

print(fruits)

print("\n------------\n")

print(fruits[0])
print(fruits[-1])
print(fruits[2])

print("\n------------\n")

print(fruits[0:3])
print(fruits[-2:])
print(fruits[1:])

print("\n------------\n")

fruits.append("fig")
fruits.remove("banana")
fruits.insert(2, "grape")
fruits.sort()
print(fruits)

print("\n-----------\n")

print(dir(fruits))
print(help(fruits.append))
