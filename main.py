from flask import Flask

app = Flask(__name__)

from model.repository.database_creator import create_database
from view.user_view import UserView




if __name__ == "__main__":
  ui = UserView()


