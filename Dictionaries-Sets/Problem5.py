student = {"python": 89, "DSA": 90, "DBMS": 88, "OS": 70}

print("Original Dict : ", student)
search = input("Enter Key : ")

student.pop(search)
print("Deleted Dict : ", student)
