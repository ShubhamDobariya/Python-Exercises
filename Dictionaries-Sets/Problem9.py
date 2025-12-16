def merge_without_overwrite(dict1, dict2):
    result = dict1.copy()

    for key, value in dict2.items():
        if key not in result:
            result[key] = value

    return result


if __name__ == "__main__":
    dict1 = {"name": "Shubham", "age": 20, "city": "Surat"}

    dict2 = {
        "age": 25,
        "country": "India",
        "grade": "A",
    }

    print(merge_without_overwrite(dict1, dict2))
