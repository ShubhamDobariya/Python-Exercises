attempts = 3
balance = 10000


while attempts > 0:
    print(f"You have {attempts} attempts left.")

    pin = int(input("Enter Your Four Digit Pin : "))

    if pin == 2709:
        amount = int(input("Enter your amount : "))

        if amount <= balance:
            balance -= amount

            print(f"Withdrawal successful! New balance = ₹{balance}")
        else:
            print("Insufficient balance!")

        break
    else:
        print("Pin Incorrect!")
        attempts -= 1


if attempts == 0:
    print("\nYour card has been blocked due to 3 incorrect attempts!")
