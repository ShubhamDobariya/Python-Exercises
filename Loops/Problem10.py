def is_prime():
    for num in range(2, 100):

        isPrime = True
        for i in range(2, num):
            if num % i == 0:
                isPrime = False

        if isPrime:
            print(num, end=" ")


if __name__ == "__main__":

    is_prime()
