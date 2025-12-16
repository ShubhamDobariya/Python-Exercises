def createList(n):
    lists = list()

    for i in range(n):
        num = int(input("Enter Number : "))
        lists.append(num)

    print("Your List : ", lists)


if __name__ == "__main__":
    n = int(input("How many numbers do you want to enter? :  "))
    createList(n)
