class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def show_status(self):
        print("Train name", self.name)
        print("Train Seats", self.seats)
        print("-----------------------------------")

    def show_fare_info(self):
        print(f"Fare per ticket : {self.fare}")
        print("-----------------------------------")

    def book_ticket(self):
        if self.seats > 0:
            self.seats -= 1
            print("Ticket Booked Successfully!")
            print("Seat Number :", self.seats + 1)
            print("-----------------------------------")
        else:
            print("Sorry, No Seats Available!")


if __name__ == "__main__":
    surat = Train("Super Fast", "1500", 5)

    surat.show_status()
    surat.show_fare_info()

    surat.book_ticket()
    surat.book_ticket()
    surat.book_ticket()
    surat.book_ticket()
    surat.book_ticket()
    surat.book_ticket()
