with open("./text.txt", "rt") as f:
    content = f.read()


content = content.replace("Donkey", "#####")

with open("./text.txt", "wt") as file:
    file.write(content)
