import random


def computer():
    option = [1, -1, 0]

    random_choice = random.choice(option)
    print(f"Computer Choice : {random_choice}")

    return random_choice


def result(user_choice, computer_choice):

    if user_choice == computer_choice:
        print("draw")
    elif (
        (user_choice == 1 and computer_choice == -1)
        or (user_choice == 0 and computer_choice == 1)
        or (user_choice == -1 and computer_choice == 0)
    ):
        print("You Win!")
    else:
        print("You loss!")


if __name__ == "__main__":
    user_choice = int(input("Choice number from (Snack(1) | Water(-1) | Gun(0)) : "))
    computer_choice = computer()
    result(user_choice, computer_choice)
