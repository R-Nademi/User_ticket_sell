from flask import Flask

app = Flask(__name__)


from view.user_view import UserView




if __name__ == "__main__":
  ui = UserView()


