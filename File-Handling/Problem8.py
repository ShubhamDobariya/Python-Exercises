file = open("./Problem7.txt", "rt")

content = file.read()

new_file = open("./Problem8.txt", "x")

new_file_write = open("./Problem8.txt", "wt")

new_file_write.write(content)

print("Successfully compleated!")
