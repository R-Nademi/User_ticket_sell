from flask import Flask, render_template,request

from controller.ticket_controller import TicketController

app = Flask(__name__, template_folder="view")

@app.route("/")
def index():
    return render_template("ticket.html")

@app.route("/tickets", methods=["POST"])
def save_ticket():
    ticket_controller = TicketController()
    status, message = ticket_controller.save(
        request.form["name"],
        request.form["family"],
        request.form["birth_date"],
        request.form["origin"],
        request.form["description"],
        request.form["start_date_time"],
        request.form["end_date_time"],
        request.form["ticket_type"],
        request.form["seat_number"],
        request.form["price"],
    )
    print(status, message)
    return render_template("ticket.html")


app.run(host="0.0.0.0", port=8080, debug=True)




if __name__ == "__main__":
    app.run(debug=True)







