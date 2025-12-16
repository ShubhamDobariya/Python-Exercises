def ReverseAndSlicing(lists):

    slicing = lists[::-1]
    print("slicing list : ", slicing)

    reverse = list()
    n = len(lists)
    for i in range(n, 0, -1):
        reverse.append(i)

    print("Reverse lists : ", reverse)


if __name__ == "__main__":
    lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    ReverseAndSlicing(lists)
