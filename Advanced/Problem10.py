Min_length = 8


while userPassword := input("Enter Your Password : "):
    if len(userPassword) < Min_length:
        print("Too short!")
    else:
        print("valid password", userPassword)
        break
