class NegativeAgeError(Exception):
    pass


def check_age(age):
    if age < 0:
        raise NegativeAgeError("Age can not be negative!")
    else:
        print("Valid age!")


try:
    age = int(input("Enter your age : "))

    check_age(age)
except NegativeAgeError as e:
    print("Custome Error : ", e)

except ValueError as e:
    print("Value Error : ", e)
