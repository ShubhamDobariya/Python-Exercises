def addStudentDetail():
    roll = input("Enter your Roll Number : ")
    name = input("Enter Your Name : ")
    age = input("Enter Your Age : ")
    mark = input("Enter Your Mark : ")

    with open("./Problem15.txt", "a") as f:
        f.write(f"{roll},{name},{age},{mark}\n")

    print("Successfully added student details.")


def retriveDetails():
    print("=================================")
    with open("./Problem15.txt", "r") as f:
        content = f.read()
        print("Student Details\n", content)


def updateStudentDetail():
    roll_to_update = input("Enter Your Roll Number : ").strip()

    updated_data = []
    found = False

    with open("./Problem15.txt", "r") as f:
        for line in f:
            roll, name, age, mark = [x.strip() for x in line.strip().split(",")]

            if roll == roll_to_update:
                print("Enter new details:")
                name = input("New Name: ")
                age = input("New Age: ")
                mark = input("New Mark: ")
                found = True

            updated_data.append(f"{roll},{name},{age},{mark}\n")

    if found:
        with open("./Problem15.txt", "w") as f:
            f.writelines(updated_data)
        print("Student record updated successfully.")
    else:
        print("Student not found.")


def show_menu():
    print("=================================")
    print("1. Add Detail : ")
    print("2. update Detail : ")
    print("3. Show Detail : ")
    print("4. Exit : ")


if __name__ == "__main__":

    while True:
        show_menu()
        query = int(input("Enter your your number : "))

        if query == 1:
            addStudentDetail()
        elif query == 2:
            updateStudentDetail()
        elif query == 3:
            retriveDetails()
        elif query == 4:
            print("Exiting system... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")
