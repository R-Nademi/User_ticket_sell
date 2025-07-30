from model.entity.ticket import Ticket

from model.repository.ticket_repository import TicketRepository







class TicketController:
    def save(self, name, family, birth_date,origin,destination,start_date_time,end_date_time,
           ticket_type,seat_number,price ):
        try:
            ticket = Ticket( name,family,birth_date,origin,destination,start_date_time,end_date_time,
                             ticket_type,seat_number,price)


            ticket_repo = TicketRepository()
            ticket_repo.save(ticket)
            return True, f"Ticket saved {ticket}"
        except Exception as e:
            return False,f"Error saving ticket {e}"

    def edit(self, code, name, family, birth_date, origin, destination, start_date_time, end_date_time,
             ticket_type, seat_number, price):
        try:
            ticket = Ticket(code,name,family,birth_date,origin,destination,start_date_time,end_date_time,
                            ticket_type,seat_number,price)

            ticket_repo = TicketRepository()
            ticket_repo.edit(ticket)
            return True, f"Ticket edited {ticket}"
        except Exception as e:
            return False,f"Error editing ticket {e}"

    def delete(self, code,name,family, birth_date, origin, destination, start_date_time, end_date_time,
               ticket_type, seat_number, price):
        try:
            ticket = Ticket(code,name,family,birth_date,origin,destination,start_date_time, end_date_time,
                            ticket_type, seat_number,price)

            ticket_repo = TicketRepository()
            ticket_repo.delete(ticket)
            return True, f"Ticket removed {ticket}"
        except Exception as e:
            return False,f"Error removing ticket {e}"

    def find_all(self):
        try:
            ticket_repo = TicketRepository()
            return True, ticket_repo.find_all()
        except Exception as e:
            return False, f"Error find all tickets {e}"

    def find_by_code(self, code):
        try:
            ticket_repo = TicketRepository()
            return True, ticket_repo.find_by_ticket(code)
        except Exception as e:
            return False, f"Error find ticket code : {code} Error :{e}"

    def find_by_name_family(self, name, family):
        try:
            ticket_repo = TicketRepository()
            return True, ticket_repo.find_by_ticket(name, family)
        except Exception as e:
            return False, f"Error find tickets name : {name} - family {family} -- Error {e}"

    def find_by_name(self, name):
        try:
            ticket_repo = TicketRepository()
            return True, ticket_repo.find_by_ticket(name)
        except Exception as e:
            return False, f"Error find tickets name : {name}  -- Error {e}"

    def find_by_password(self, name, password):
        try:
            ticket_repo = TicketRepository()
            return True, ticket_repo.find_by_password(name,password)
        except Exception as e:
            return False, f"Error find tickets  name:password : {name}:{password}  -- Error {e}"





