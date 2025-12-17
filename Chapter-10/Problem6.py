class Student:
    def __init__(harry, name, enrollmentNo, age):
        harry.name = name
        harry.enrollmentNo = enrollmentNo
        harry.age = age

    def show_info(harry):
        print(f"Name : {harry.name}")
        print(f"EnrollmentNo : {harry.enrollmentNo}")
        print(f"Age : {harry.age}")
        print("---------------------------------------------")


if __name__ == "__main__":
    s1 = Student("Shubham", 18, 20)
    s2 = Student("Parth", 49, 21)
    s3 = Student("Harsh", 25, 23)
    s4 = Student("Tirth", 8, 19)

    s1.show_info()
    s2.show_info()
    s3.show_info()
    s4.show_info()
