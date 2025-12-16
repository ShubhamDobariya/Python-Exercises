def is_prime(num):
    if num <= 1:
        isPrime = False
    else:
        isPrime = True
        for i in range(2, num):
            if num % i == 0:
                isPrime = False
                break

    if isPrime == True:
        print(f"{num} is Prime Number!")
    else:
        print(f"{num} is not Prime Number!")


if __name__ == "__main__":
    num = int(input("Enter Number : "))
    is_prime(num)
