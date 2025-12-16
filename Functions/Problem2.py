def even_odd(num):
    if num % 2 == 0:
        print(f"{num} is Even Number!")
    else:
        print(f"{num} is Odd Number!")


if __name__ == "__main__":
    num = int(input("Enter Number : "))
    even_odd(num)
