def SplitEvenOdd(lists):

    evenList = list()
    oddList = list()

    for num in lists:
        if num % 2 == 0:
            evenList.append(num)

        if num % 2 != 0:
            oddList.append(num)

    print("Even List : ", evenList)
    print("Odd List : ", oddList)


if __name__ == "__main__":
    lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    SplitEvenOdd(lists)
