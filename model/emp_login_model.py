class Emp_info:
    def __init__(self, fname="", lname="", address="", gender="", mobile="", username="", password=""):
        # self.__id = id
        self.__fname = fname
        self.__lname = lname
        self.__address = address
        self.__gender = gender
        self.__mobile = mobile
        self.__username = username
        self.__password = password

    # def set_id(self, id):
    #     self.__id = id
    def set_fname(self, fname):
        self.__fname = fname
    def set_lname(self, lname):
        self.__lname = lname
    def set_address(self, address):
        self.__address = address
    def set_gender(self, gender):
        self.__gender = gender
    def set_mobile(self, mobile):
        if type(mobile) is not(int):
            raise TypeError("Please insert an integer value and try again.")
        else:
            self.__mobile = mobile
    def set_username(self, username):
        self.__username = username
    def set_password(self, password):
        self.__password = password

    # def get_id(self):
    #     return self.__id
    def get_fname(self):
        return self.__fname
    def get_lname(self):
        return self.__lname
    def get_address(self):
        return self.__address
    def get_gender(self):
        return self.__gender
    def get_mobile(self):
        return self.__mobile
    def get_username(self):
        return self.__username
    def get_password(self):
        return self.__password