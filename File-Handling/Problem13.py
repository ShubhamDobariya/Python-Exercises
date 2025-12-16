num = int(input("Enter Number : "))

file = open("./Problem13.txt", "x")

with open("./Problem13.txt", "wt") as file_write:
    for i in range(1, 11):
        file_write.write(f"{num} X {i} = {num*i}\n")


file_write.close()
