def remove_and_strip(list):
    clean_list = []

    for item in list:
        new_item = item.strip()
        clean_list.append(new_item)

    return clean_list


if __name__ == "__main__":
    list = ["  shubham", "apple  ", " orange ", "banana"]

    print(remove_and_strip(list))
