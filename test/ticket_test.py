from model.entity.ticket import Ticket
from controller.ticket_controller import TicketController
from test.user_test import message



ticket_controller = TicketController()


status,message = ticket_controller.save(1, "Ali", "AliPour",
                   "1360", "Mashhad",
           "Tehran", "10.30", "12.00",
                "Airline","A21","30$")


print(message)


def __repr__(self):
    return f"{self.__dict__}"

