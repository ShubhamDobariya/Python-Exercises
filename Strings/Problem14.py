# 15. Build a mini program that validates an email address using string operations.


def EmailValidates(email):
    atsign = "@"
    dotsign = "."

    if atsign in email and dotsign in email:

        atsignCount = 0

        for ch in email:
            if ch == atsign:
                atsignCount += 1

        if atsignCount != 1:
            print("Email must be contain one @")
            return

        # Split into local part and domain part
        local, domain = email.split("@")

        if len(local) == 0:
            print("Invalid: Nothing before '@'")
            return

        if len(domain) == 0:
            print("Invalid: Nothing after '@'")
            return

        if "." not in domain:
            print("Invalid: Domain must contain '.'")
            return

        print("Valid Email ✔")

    else:
        print("Your email is not valid ")


if __name__ == "__main__":
    email = input("Enter your Email : ")

    EmailValidates(email)
