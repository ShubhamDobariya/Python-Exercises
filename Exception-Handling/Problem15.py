class InvalidPinError(Exception):
    pass


class InsufficientBalanceError(Exception):
    pass


def atm_system():
    correct_pin = 2709
    balance = 5000

    try:
        pin = int(input("Enter Your correct PIN : "))
        if pin != correct_pin:
            raise InvalidPinError("Invalid PIN!")

    except (ValueError, InvalidPinError) as e:
        print("Login Failed!", e)
        return

    print("\nLogin successful ✅")

    while True:
        try:
            print("====ATM MENU=====")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            print("=================")

            choice = int(input("Enter your choice : "))

            if choice == 1:
                print(f"Current Balance ₹{balance}")
                print("=============================")

            elif choice == 2:
                amount = int(input("Enter Your Amount : "))
                if amount < 0:
                    raise ValueError("Deposit amount must be positive!")

                balance += amount
                print(f"₹{amount} deposited successfully.")
                print("====================================")

            elif choice == 3:
                amount = int(input("Enter amount to withdraw: "))

                if amount <= 0:
                    raise ValueError("Withdrawal amount must be positive.")

                if amount > balance:
                    raise InsufficientBalanceError("Insufficient balance!")

                balance -= amount

                print(f"₹{amount} withdrawn successfully.")
                print("===================================")

            elif choice == 4:
                print("Thank you for using the ATM. Goodbye!")
                break

            else:
                raise ValueError("Invalid menu choice!")

        except ValueError as e:
            print("Input Error:", e)

        except InsufficientBalanceError as e:
            print("Transaction Error: ", e)

        except Exception as e:
            print("Unexpected Error: ", e)

        finally:
            print("ATM is ready for next operation...\n")


if __name__ == "__main__":
    atm_system()
