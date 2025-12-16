def showMenu():
    print("1. Add to Cart.")
    print("2. Show Product.")
    print("3. Exit.")


def AddToCart(lists):
    name = input("Enter Product Name : ")
    qty = int(input("Enter Quantity : "))
    price = int(input("Enter Product Price : "))

    tuples = (name, qty, price)

    lists.append(tuples)

    return lists


def ShowProducts(lists):
    print("List Of Products : ", lists)


if __name__ == "__main__":
    lists = []

    while True:
        showMenu()
        choice = int(input("Choice from Menu: "))

        if choice == 1:
            AddToCart(lists)

        elif choice == 2:
            ShowProducts(lists)

        elif choice == 3:
            print("Thank you! Exiting...")
            break

        else:
            print("Invalid choice! Try again.")
