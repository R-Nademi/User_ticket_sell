def save(self, code, name, family, username, password, role, locked):
    try:
        connection = sqlite3.connect("ticket_db.sqlite")
        cursor = connection.cursor()
        self.connect()
        self.cursor.execute(
                """insert into users,
                       (code, name, family, username, password, role, locked)
                   values (?, ?, ?, ?, ?, ?, ?)""",
            [code, name, family, username, password, role, locked])
        connection.commit()
        cursor.close()
        connection.close()
        return True, f"User saved"
    except Exception as e:
        return False, f"Error saving user {e}"