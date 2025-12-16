name = input("Enter Your Name : ")


if len(name) < 3 or len(name) > 15:
    print("Username length must be between 3 and 15 characters.")


for ch in name:
    if not (ch.isalnum() or ch == "_"):
        print("Username can contain only letters, numbers, and underscore (_).")
        break
    else:
        print("Valid username ✔")
        break
