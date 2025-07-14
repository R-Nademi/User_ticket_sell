import os

from model.entity.ticket import Ticket
from model.repository.database_creator import create_database
from view.ticket_view import TicketView


create_database()

ui = TicketView()
