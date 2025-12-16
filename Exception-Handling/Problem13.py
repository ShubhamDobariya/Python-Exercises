class LoginAttemptsExceeded(Exception):
    pass


def check():
    correct_username = "admin"
    correct_password = "12345"

    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        username = input("Enter your username : ")
        password = input("Enter your password : ")

        if username == correct_username and password == correct_password:
            print("Login successful")
            return
        else:
            attempts += 1
            print(f"Invalid credentials (Attempt {attempts}/{max_attempts})")

    raise LoginAttemptsExceeded("Too many failed login attempts. Account locked!")


if __name__ == "__main__":
    try:
        check()
    except LoginAttemptsExceeded as e:
        print("Login Error:", e)
