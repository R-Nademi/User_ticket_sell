import sqlite3



def save(self, code, name, family,birth_date,origin, destination,start_date_time,end_date_time,ticket_type,price):
    try:
        connection = sqlite3.connect("ticket_db.sqlite")
        cursor = connection.cursor()
        self.connect()
        self.cursor.execute(
                """,insert into tickets,
                       (code, name, family, birth_date,origin,destination,start_date-time,end_date-time,
                       ticket_type,seat_number,price)
                   values (?, ?, ?, ?, ?, ?, ?)""",
            [code, name, family, birth_date, origin, destination, start_date_time, end_date_time, ticket_type, price ])
        connection.commit()
        cursor.close()
        connection.close()
        return True, f"ticket saved"
    except Exception as e:
        return False, f"Error saving ticket {e}"