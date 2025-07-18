from model.tools.validation import name_validator



class Patient():
    def __init__(self, code, name, family,phone_number):
        self.code = code
        self.name = name
        self.family = family
        self.phone_number = phone_number


    @property
    def code(self):
        return  self._code

    @code.setter
    def code(self, value):
        code_validator(value)
        self._code = value

    @property
    def name(self):
        return  self._name


    @name.setter
    def name(self, value):
        name_validator(value)
        self._name = value


    @property
    def family(self):
        return   self._family


    @family.setter
    def family(self, value):
        family_validation(value)
        self._family = value


    @property
    def phone_number(self):
         return  self._phone_number


    @phone_number.setter
    def phone_number(self, value):
        phone_number_validation(value)
        self._phone_number = value




    def __repr__(self):
        return f"{self.__dict__}"
