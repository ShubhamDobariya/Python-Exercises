def SumOfList(list):
    sum = 0

    for num in list:
        sum += num

    print(f"Sum of given list is {sum}")


if __name__ == "__main__":
    list = [12, 32, 45, 56, 76, 89]

    SumOfList(list)
