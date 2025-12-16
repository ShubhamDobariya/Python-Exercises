sorted_mark = []


for i in range(1, 6):
    mark = int(input(f"Enter student {i} mark : "))
    sorted_mark.append(mark)

sorted_mark.sort()

print(sorted_mark)
