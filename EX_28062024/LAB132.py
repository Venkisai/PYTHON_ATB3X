class Password:
    def __init__(self,password):
        self.__password = password
        self.public_var = 10

    def get_password(self, is_auth):
        if is_auth:
            print(self.__password)
        else:
            print("Not a valid password")

    def set_password(self, password):
        if len(password) > 10:
            self.__password = password
            print("set to correct", self.__password)
        else:
            print("Not allowed, its a weak password")
pwd = Password("Hacker123")
pwd.get_password(False)
pwd.set_password("Venkat!123@456")