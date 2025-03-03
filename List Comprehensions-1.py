numbers = [1, 2, 3, 4, 5]

squared_numbers = [x **2 for x in numbers]

print(squared_numbers)

print("\n------------\n")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)

print("\n------------\n")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

modified_numbers = [x if x % 2 == 0 else "odd" for x in numbers]

print(modified_numbers)

print("\n------------\n")

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

pairs = [(x,y) for x in list1 for y in list2]

print(pairs)

print("\n------------\n")

def square(n):
    return n ** 2

numbers = [1, 2, 3, 4, 5]

squared_numbers = [square(x) for x in numbers] 

print(squared_numbers)