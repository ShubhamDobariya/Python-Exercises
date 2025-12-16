def show_menu():
    print("1. Add a Visitor")
    print("2. Show All Unique Visitors")
    print("3. Show Total Unique Visitors")
    print("4. Exit")


def add_visitor(visitors):
    name = input("Enter visitor name: ").strip()

    if name == "":
        print("Invalid name! Try again.")

    if name in visitors:
        print(f"Visitor '{name}' already visited.")
    else:
        visitors.add(name)
        print(f"Visitor '{name}' added.")


def show_visitors(visitors):
    for visitor in visitors:
        print("-", visitor)


def total_unique(visitors):
    print(f"Total unique visitors: {len(visitors)}")


if __name__ == "__main__":
    visitors = set()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_visitor(visitors)
        elif choice == "2":
            show_visitors(visitors)
        elif choice == "3":
            total_unique(visitors)
        elif choice == "4":
            print("Exiting visitor tracker... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
