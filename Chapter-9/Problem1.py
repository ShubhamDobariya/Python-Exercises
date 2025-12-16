file = open("./poems.txt", "rt")
content = file.read()

print(content)
print("-------------------------------------------")

if "twinkle" in content:
    print("'twinkle' is present in this file.")
else:
    print("'twinkle' is not present in this file.")
