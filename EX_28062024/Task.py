class Company:

    Name = None
    Id = None
    Address = None

    def __init__(self, Name, Id, Address):
        self.name = Name
        self.Id = Id
        self.Address = Address

    def place(self):
        print("name of the company is:\n" + self.name)
        print("id of the company is:\n" + self.Id)
        print("Location of the company is:\n" + self.Address)


C1 = Company("JP MORGAN CHASE AND CO.", "JPMC", "UNITED STATES OF AMERICA")
C1.place()

C2 = Company("BARCLAYS", "BARCY", "UNITED KINGDOM")
C2.place()

C3 = Company("GOLDMANSACHS", "GSH", "CANADA")
C3.place()

