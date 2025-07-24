from dbm import sqlite3

from flask import Flask


app = Flask(__name__)


from view.ticket_view import TicketView




if __name__ == "__main__":
  ui = TicketView()


