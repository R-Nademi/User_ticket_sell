class Patient():
    def __init__(self, code, name, family,phone_number):
        self.code = code
        self.name = name
        self.family = family
        self.phone_number = phone_number


    # todo : getter/setter ---> validation

    def __repr__(self):
        return f"{self.__dict__}"
