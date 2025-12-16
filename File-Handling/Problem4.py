file = open("./Problem3.txt", "rt")

content = file.read()

total_word = len(content.split())
total_ch = len(content)


print("Total world :", total_word)
print("Total ch :", total_ch)
