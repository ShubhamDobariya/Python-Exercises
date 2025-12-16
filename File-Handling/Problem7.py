language = input("Enter One Programming Language : ")


file = open("./Problem7.txt", "rt")

content = file.read().lower()

new_content = content.replace("python", language)

new_file = open("./Problem7.txt", "wt")

new_file.write(new_content)

print(f"'{language}' has been replaced with Python successfully.")
