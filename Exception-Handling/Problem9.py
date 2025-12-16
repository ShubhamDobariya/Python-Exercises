class InsufficientBalanceError(Exception):
    pass


def check_balance(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance for this withdrawal.")
    else:
        balance -= amount
        print(f"Withdrawal successful! Remaining balance: ₹{balance}")
        return balance


if __name__ == "__main__":
    balance = 5000

    try:
        print(f"Current Balance is {balance}")

        amount = int(input("Enter withdrawal amount : "))

        balance = check_balance(balance, amount)
    except InsufficientBalanceError as e:
        print("Custome Error : ", e)

    except ValueError as e:
        print("Value error", e)

    else:
        print(f"Balance ₹{balance}")
