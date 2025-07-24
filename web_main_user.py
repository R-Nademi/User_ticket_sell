from flask import Flask, render_template,request

from controller.user_controller import UserController

app = Flask(__name__, template_folder="view")

@app.route("/")
def index():
    return render_template("user.html")

@app.route("/users", methods=["POST"])
def save_user():
    user_controller = UserController()
    status, message = user_controller.save(
        request.form["name"],
        request.form["family"],
        request.form["username"],
        request.form["password"],
        request.form["role"],
        False
    )
    print(status, message)
    return render_template("user.html")


app.run(host="0.0.0.0", port=8080, debug=True)




if __name__ == "__main__":
    app.run(debug=True)







