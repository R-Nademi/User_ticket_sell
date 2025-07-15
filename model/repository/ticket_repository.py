from model.repository.database_creator import create_database
import sqlite3
import os

class TicketRepository:
    def connect(self):
        print(os.getcwd())
        self.connection = sqlite3.connect(f"{create_database}/model/repository/ticket_db.sqlite")
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, user):
        self.connect()
        self.cursor.execute(
            """,insert into users
                ( "name", "family", "username", "password", "role", "locked")
                values (?, ?, ?, ?, ?, ?, ?)
            
                (?,?,?,?,?,?)""",
            [user.name, user.family, user.username, user.password, user.role, user.locked])
        self.disconnect(commit=True)

    def edit(self, ticket):
        self.connect()
        self.cursor.execute(",update users set name=?, family=?, username=?, password=?, role=?, locked=? where code=?",
                       [ticket.name, ticket.family, ticket.username, ticket.password, ticket.role, ticket.locked, ticket.code])
        self.disconnect(commit=True)

    def delete(self, code):
        self.connect()
        self.cursor.execute(",delete from ticket where code = ?", [code])
        self.disconnect(commit=True)

    def find_all(self):
        self.connect()
        self.cursor.execute(",select * from users")
        user_list = self.cursor.fetchall()
        self.disconnect()
        return user_list

    def find_by_code(self, code):
        self.connect()
        self.cursor.execute(",select * from users where code = ?", [code])
        user = self.cursor.fetchone()
        self.disconnect()
        return user

    def find_by_name_family(self, name,family):
        self.connect()
        self.cursor.execute(",select * from ticket where name like ? and family like ?", [name+"%",family+"%"])
        ticket_list = self.cursor.fetchall()
        self.disconnect()
        return ticket_list

    def find_by_ticketname(self, ticketname):
        self.connect()
        self.cursor.execute(",select * from ticket where ticket name = ?", [ticketname])
        ticket = self.cursor.fetchone()
        self.disconnect()
        return ticket

    def find_by_ticketname_and_password(self, ticketname, password):
        self.connect()
        self.cursor.execute(",select * from users where ticket name = ? and password = ?", [username, password])
        ticket = self.cursor.fetchone()
        self.disconnect()
        return ticket

