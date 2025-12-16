def MergeTwoList(list1, list2):

    # list1.extend(list2)

    for num in list2:
        list1.append(num)

    return list1


if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]

    print(MergeTwoList(list1, list2))
