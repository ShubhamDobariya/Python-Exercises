search = input("Enter word to search: ")

file = open("./Problem9.txt", "rt")

for index, line in enumerate(file.readlines()):
    if search.lower() in line.lower():
        print(f"Index of your {search} is {index}.")
