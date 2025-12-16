badword_list = ["Donkey", "bad", "stupid", "badword", "badboy"]


with open("./words.txt", "rt") as read_file:
    content = read_file.read()


for word in badword_list:
    content = content.replace(word, "#####")

with open("./words.txt", "wt") as write_files:
    write_files.write(content)
