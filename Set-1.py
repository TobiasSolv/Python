fruits = {"apple", "banana", "cherry"}

print("\n")

print(fruits)

print("\n------------\n")

numbers = {1,2,3}

numbers.add(4)
numbers.remove(2)
numbers.discard(5)

print(numbers)

print("\n------------\n")

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set3 = set1.union(set2)

print(set3)

set4 = set1.intersection(set2)

print(set4)

print("\n------------\n")

colors = {"red", "blue", "green"}

if "yellow" in colors:
        print("Yellow is in the set")
else:
        print("Yellow is not in the set")

if "blue" in colors:
        print("Blue is in the set")
else:
        print("Blue is not in the set")

print("\n------------\n")

help(set)
print(dir(set))