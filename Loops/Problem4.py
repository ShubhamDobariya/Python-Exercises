def MultiplicationTable(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")


if __name__ == "__main__":
    n = int(input("Enter Number : "))
    MultiplicationTable(n)
