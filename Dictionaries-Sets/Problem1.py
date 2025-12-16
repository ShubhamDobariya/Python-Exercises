student = {
    "name": "Shubham",
    "age": 20,
    "course": "AIML",
    "city": "Surat",
    "grade": "A",
}


for key in student.keys():
    print(key, " | ", end=" ")


print("\n")

for value in student.values():
    print(value, " | ", end=" ")
