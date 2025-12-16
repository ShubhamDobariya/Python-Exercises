search = input("Enter word to search: ")


file = open("./Problem6.txt", "rt")

content = file.read()

if search.lower() in content.lower():
    print(f"{search} word is exist in this file.")
else:
    print(f"{search} word does not exist in this file.")
