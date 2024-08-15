#In case of API Automation

class VWOLoginPage:
    Username = None
    Password = None

    def __init__(self, Username, Password):
        self.Username = Username
        self.Password = Password

    def Login_Confirm(self):
        if self.Password == "pass456":
            print("Your are allowed")
        else:
            print("Not allowed")


Venkat = VWOLoginPage("Venkat78", "pass556")
Venkat.Login_Confirm()