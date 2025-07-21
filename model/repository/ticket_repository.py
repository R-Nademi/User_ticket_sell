import os
import sqlite3



class TicketRepository:
    def __init__(self):
        self.connection = None
        self.cursor = None


    def connect(self):
        print(os.getcwd())
        self.connection = sqlite3.connect("model/repository/ticket_db.sqlite")
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
                (code,name,family,birth_date,origin,description,start_date_time,end_date_time,ticket_type,seat_number,price) 
            values
                (?,?,?,?,?,?)""",
            [ticket.code, ticket.name, ticket.family, ticket.birth_date, ticket.origin, ticket.description,
             ticket.start_date_time,ticket.end_date_time,ticket.ticket_type,ticket.seat_number,ticket.price])
        self.disconnect(commit=True)

    def edit(self, ticket):
        self.connect()
        self.cursor.execute(",update tickets set name=?, family=?, ticket_list=?, password=?, role=?, locked=? where code=?",
                       [ticket.name, ticket.family, ticket.birth_date, ticket.origin, ticket.description,ticket.start_date_time,
                        ticket.end_date_time,ticket.ticket_type,ticket.seat_number,ticket.price])
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

    def find_by_ticket(self, ticket):
        self.connect()
        self.cursor.execute(",select * from tickets where ticket = ?", [ticket])
        ticket = self.cursor.fetchone()
        self.disconnect()
        return ticket

    def find_by_ticket_and_password(self, ticket, password):
        self.connect()
        self.cursor.execute(",select * from tickets where ticket = ? and password = ?", [ticket, password])
        ticket = self.cursor.fetchone()
        self.disconnect()
        return ticket

