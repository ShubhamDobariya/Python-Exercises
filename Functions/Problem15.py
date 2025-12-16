def deposit(money):
    print(f"Your {money} money is successfully deposit!")


def withdraw(money):
    print(f"Your {money} money is successfully withdraw!")


if __name__ == "__main__":
    option = int(input("Choice what you do [deposit(1)] or [withdraw(-1)] : "))
    money = int(input("Enter your Money : "))

    if option == 1:
        deposit(money)

    if option == -1:
        withdraw(money)
