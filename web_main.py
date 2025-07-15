from flask import Flask, render_template,request

from controller.ticket_controller import TicketController

app = Flask(__name__, template_folder="view")

@app.route("/")
def index():
    return render_template("ticket.html")

@app.route("/ticket", methods=["POST"])
def save_ticket():
    ticket_controller = TicketController()
    status, message = ticket_controller.save(
        request.form["name"],
        request.form["family"],
        request.form["username"],
        request.form["password"],
        request.form["role"],
        False
    )
    print(status, message)
    return render_template("ticket.html")



app.run(host="192.168.39.100", port=80, debug=True)