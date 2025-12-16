student = {"python": 89, "DSA": 90, "DBMS": 88, "OS": 70}


search = input("Enter Subject Name : ")

if search in student.keys():
    print(student[search])
