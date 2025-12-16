class PasswordLengthError(Exception):
    pass


def check_password_len(password):
    if len(password) < 8:
        raise PasswordLengthError("Password length is less than 8")
    else:
        print("Valid Password")


try:
    password = input("Enter Your Password : ")
    check_password_len(password)

except PasswordLengthError as e:
    print("Custome Error : ", e)

else:
    print(password)
