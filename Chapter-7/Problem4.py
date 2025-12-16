def isPrime(n):
    if n <= 1:
        print(f"{n} is not prime number!")

    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not prime number!")

    print(f"{n} is prime number!")


if __name__ == "__main__":
    n = 10

    isPrime(n)
