import string


def PasswordValidate():
    password = input("Enter Your Password : ")

    has_lower = any(ch.islower() for ch in password)
    has_upper = any(ch.isupper() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    has_special = any(ch in string.punctuation for ch in password)
    has_long = len(password) > 8

    if not has_lower:
        print("Password must be contain lower character")
        return PasswordValidate()
    if not has_upper:
        print("Password must be contain upper character")
        return PasswordValidate()
    if not has_digit:
        print("Password must be contain digit character")
        return PasswordValidate()
    if not has_special:
        print("Password must be contain special character")
        return PasswordValidate()
    if not has_long:
        print("Password must be more than 8 character")
        return PasswordValidate()

    print("Password was successfully created!")


if __name__ == "__main__":

    PasswordValidate()
