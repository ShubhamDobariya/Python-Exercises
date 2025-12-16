def RemoveDuplicate(lists):

    seen = set()

    for num in lists:
        if num not in seen:
            seen.add(num)

    return list(seen)


if __name__ == "__main__":
    lists = [1, 2, 3, 4, 5, 4, 3, 2, 6, 7, 8, 2]

    print(RemoveDuplicate(lists))
