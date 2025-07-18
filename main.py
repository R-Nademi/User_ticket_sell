import database_creator

from model.repository.database_creator import create_database
from view.user_view import UserView


create_database()


if __name__ == "__main__":
  ui = UserView()


