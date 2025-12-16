file7 = open("./Problem7.txt", "rt")

file8 = open("./Problem8.txt", "rt")

file9 = open("./Problem9.txt", "wt")

file9.write(file7.read())
file9.write("\n")
file9.write(file8.read())


print("Successfully Merge Two Files.")
