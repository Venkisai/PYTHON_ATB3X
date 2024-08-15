class VWOlogin:
    email = None
    password = None

    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    def login_confirm(self):
        if self.__email == "abc@gmail.com" and self.__password == 123:
            print("You are Allowed")
        else:
            print("You are not allowed")


page = VWOlogin("abcd@gmail.com", 123)
page.login_confirm()