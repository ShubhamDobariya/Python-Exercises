def CountNuOfvowels(str):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0

    for s in str:
        if s in vowels:
            count += 1

    print(f"Total Number of Vowels {count}")


if __name__ == "__main__":
    str = input("Enter Your string : ")
    CountNuOfvowels(str)
