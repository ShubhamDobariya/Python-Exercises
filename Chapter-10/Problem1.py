class Programmer:
    company = "Microsoft"

    def __init__(self, name, language, experience):
        self.name = name
        self.language = language
        self.experience = experience

    def show_detail(self):
        print(self.name)
        print(self.language)
        print(self.experience)
        print("----------------")


if __name__ == "__main__":
    p1 = Programmer("Shubham", "Python", 2)
    p2 = Programmer("Rishit", "Java", 1)

    p1.show_detail()
    p2.show_detail()
