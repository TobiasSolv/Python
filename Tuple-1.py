my_tuple = (42, 3.14, "hello", True)

print("\n")

print(my_tuple)

print("\n------------\n")

sample_tuple = ("apple", 7, 3.5, "banana")

print(sample_tuple[1])
print(sample_tuple[-1])

last_element = sample_tuple[-1]

print(last_element)

print("\n------------\n")

person = ("Alice", 25, "Engineer")

name, age, profession = person

print(name)
print(age)
print(profession)

print("\n------------\n")

print(dir(()))
help((1,2).index)