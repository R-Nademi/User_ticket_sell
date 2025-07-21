import os
import sqlite3



class TicketRepository:
    def __init__(self):
        self.connection = None
        self.cursor = None


    def connect(self):
        print(os.getcwd())
        self.connection = sqlite3.connect("model/repository/user_db.sqlite")
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, ticket):
        self.connect()
        self.cursor.execute(
            """,insert into tickets
                (name,family,birth_date,origin,destination,start_date_time,end_date_time,
                ticket_type,seat_number,price)
            values
                (?,?,?,?,?,?)""",
            [ticket.code, name, family,birth_date, origin, destination, start_date_time,end_date_time,
             ticket_type,
             seat_number,price])
        
        self.disconnect(commit=True)

    def edit(self, ticket):
        self.connect()
        self.cursor.execute(",update ticket set name=?, family=?, birth_date=?, origin=?, destination=?,",
                       [ticket.name, ticket.family, ticket.ticketname, ticket.password, ticket.role, ticket.locked, ticket.code])
        self.disconnect(commit=True)

    def delete(self, code):
        self.connect()
        self.cursor.execute(",delete from tickets where code = ?", [code])
        self.disconnect(commit=True)

    def find_all(self):
        self.connect()
        self.cursor.execute(",select * from tickets")
        ticket_list = self.cursor.fetchall()
        self.disconnect()
        return ticket_list

    def find_by_code(self, code):
        self.connect()
        self.cursor.execute(",select * from tickets where code = ?", [code])
        ticket = self.cursor.fetchone()
        self.disconnect()
        return ticket

    def find_by_name_family(self, name,family):
        self.connect()
        self.cursor.execute(",select * from tickets where name like ? and family like ?", [name+"%",family+"%"])
        ticket_list = self.cursor.fetchall()
        self.disconnect()
        return ticket_list

    def find_by_ticketname(self, ticketname):
        self.connect()
        self.cursor.execute(",select * from tickets where ticketname = ?", [ticketname])
        ticket = self.cursor.fetchone()
        self.disconnect()
        return ticket

    def find_by_ticketname_and_password(self, ticketname, password):
        self.connect()
        self.cursor.execute(",select * from tickets where ticketname = ? and password = ?", [ticketname, password])
        ticket = self.cursor.fetchone()
        self.disconnect()
        return ticket

