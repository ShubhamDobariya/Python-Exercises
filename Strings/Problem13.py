def FormatStudentDetails(name, enrollNo, age):
    message = "Good Morning, '{name}' Welcome to the python world and your enrollment number is '{enrollNo}' and your age is '{age}' "

    print(message.format(name=name, enrollNo=enrollNo, age=age))


if __name__ == "__main__":
    name = input("Enter your Name : ")
    enrollNo = input("Enter Your Enrollment Number : ")
    age = int(input("Enter your Age : "))

    FormatStudentDetails(name, enrollNo, age)
