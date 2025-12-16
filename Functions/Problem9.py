def CountVowels(str):
    strs = str.lower()
    vowels = ["a", "e", "i", "o", "u"]
    count = 0

    for s in strs:
        if s in vowels:
            count += 1

    print(f"Total vowels are {count}")


if __name__ == "__main__":
    str = input("Enter String : ")
    CountVowels(str)
