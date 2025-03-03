"""
with open ("example.txt", "r") as f: 
    content = f.read()

    print(content)

with open("output.txt", "w") as f: 
    content = "Hello, Python!"
    f.write(content)

    print(content)

with open("output.txt", "a") as f: 
    content = "This is an addition!"
    f.write(content)

    print(content)

with open("output.txt", "r") as f: 
    content = f.read()

    print(content)
    print(dir(f))
    help(f.read)

with open("combined.txt", "w") as f: 
    content = "Starting fresh!"
    f.write(content)

with open("combined.txt", "a") as f: 
    content = "\nAppending new data!"
    f.write(content)

with open("combined.txt", "r") as f:
    content = f.read()

    print(content)


try:

    with open("non_existent.txt", "r") as f:
        f.read()

except: 
    print("File not found!")



with open("large_file.txt", "r") as f:
    for line in f:  # Loop through each line in the file
        print(line, end="")  # Print line without extra newlines

 
"""       

with open("data.txt", "w") as f:
    f.write("""
line 1
line 2
line 3
""")
    
with open("data.txt", "r") as f:
    for line in f:  
        print(line, end="")  