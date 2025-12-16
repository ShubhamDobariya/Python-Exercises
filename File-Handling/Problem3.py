file = open("./Problem3.txt", "rt")

count = 0

for line in file.readlines():
    count += 1


print("Total lines ", count)
