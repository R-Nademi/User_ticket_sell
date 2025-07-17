import os




from model.repository.database_creator import create_database
from view.user_view import UserView


create_database()

ui = UserView()
