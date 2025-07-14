from model.tools.validation import *





class User:
    def init(self, code, name, family, username,password,role):
        self.code = code
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.role = role



    def repr(self):
        return f"{self.dict}"

    def to_tuple(self):
        return tuple(self.dict.values())


    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        code_validation(value)
        self._code = value

    @property
    def name(self):
        return  self._name

    @name.setter
    def name(self, value):
        name_validation(value)
        self._name = value

    @property
    def family(self):
        return  self._family

    @family.setter
    def family(self, value):
        family_validation(value)
        self._family = value

    @property
    def username(self):
        return  self._username

    @username.setter
    def username(self, value):
        username_validation(value)
        self._username = value

    @property
    def password(self):
        return  self._password

    @password.setter
    def password(self, value):
        password_validation(value)
        self._password = value

    @property
    def role(self):
        return  self._role

    @role.setter
    def role(self, value):
        role_validation(value)
        self._role = value