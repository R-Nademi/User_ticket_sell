from model.repository.database_creator import main_path
import sqlite3

class UserRepository:
    def connect(self):
        print(os.getcwd())
        self.connection = sqlite3.connect(f"{main_path}/model/repository/sell_db.sqlite")
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()

    def save(self, user):
        self.connect()
        self.cursor.execute(
        """insert into users,
           ( name, family, username, password, role, locked)
           values
           (?,?,?,?,?,?)""",
            [user.name, user.family, user.username, user.password, user.role, user.locked])
        self.disconnect(commit=True)

    def edit(self, user):
        self.connect()
        self.cursor.execute("update users set name=?, family=?, username=?, password=?, role=?, locked=? where code=?",
                       [user.name, user.family, user.username, user.password, user.role, user.locked, user.code])
        self.disconnect(commit=True)

    def delete(self, code):
        self.connect()
        self.cursor.execute("delete from users where code = ?", [code])
        self.disconnect(commit=True)

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from users")
        user_list = self.cursor.fetchall()
        self.disconnect()
        return user_list

    def find_by_code(self, code):
        self.connect()
        self.cursor.execute("select * from users where code = ?", [code])
        user = self.cursor.fetchone()
        self.disconnect()
        return user

    def find_by_name_family(self, name,family):
        self.connect()
        self.cursor.execute("select * from users where name like ? and family like ?", [name+"%",family+"%"])
        user_list = self.cursor.fetchall()
        self.disconnect()
        return user_list

    def find_by_username(self, username):
        self.connect()
        self.cursor.execute("select * from users where username = ?", [username])
        user = self.cursor.fetchone()
        self.disconnect()
        return user

    def find_by_username_and_password(self, username, password):
        self.connect()
        self.cursor.execute("select * from users where username = ? and password = ?", [username, password])
        user = self.cursor.fetchone()
        self.disconnect()
        return user

