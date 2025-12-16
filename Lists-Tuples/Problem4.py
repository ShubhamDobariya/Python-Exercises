def SortArray(lists):
    n = len(lists)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            if lists[j] < lists[min_idx]:
                min_idx = j

        lists[i], lists[min_idx] = lists[min_idx], lists[i]

    return lists


if __name__ == "__main__":
    lists = [122, 54, 35, 57, 67, 54, 89, 67, 98, 654, 89]
    print(SortArray(lists))
