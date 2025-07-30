from controller.ticket_controller import TicketController
ticket_controller = TicketController()





status,message = ticket_controller.save(1, "Ali", "AliPour",
                   "1360", "Mashhad",
           "Tehran", "10.30", "12.00",
                "Airline","A21","30$")



