from model.tools.validation import (name_validator, family_validator, code_validator,
                                    birth_date_validator,origin_validator,description_validator,
                                    start_date_time_validatorend_date_time_validator,
                                    ticket_type_validator,price_validator)


class Patient:
    def __init__(self, code, name, family,birth_date,origin,description,
                 start_date_time,end_date_time,ticket_type,price):
        self.code = code
        self.name = name
        self.family = family
        self.birth_date = birth_date
        self.origin = origin
        self.description = description
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.ticket_type = ticket_type
        self.price = price


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
        family_validator(value)
        self._family = value


    @property
    def birth_date(self):
        return   self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        birth_date_validator(value)
        self._birth_date = value


    @property
    def origin(self):
        return    self._origin

    @origin.setter
    def origin(self, value):
        origin_validator(value)
        self._origin = value


    @property
    def description(self):
        return    self._description


    @description.setter
    def description(self, value):
        description_validator(value)
        self._description = value














    def __repr__(self):
        return f"{self.__dict__}"
