from model.entity.user import User


user = User(1, "Ali", "AliPour",
                   "1360", "Mashhad",
           "Tehran", "10.30", "12.00",
                "Airline","A21","30$")


print(user)


def __repr__(self):
    return f"{self.__dict__}"
