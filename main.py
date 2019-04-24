from flask import Flask, render_template, request, redirect, url_for
from models import User

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")



@app.route("/login", methods=["POST"])
def login():
    name = request.form.get("user-name")
    email = request.form.get("user-email")

    # create a User object
    user = User(name=name, email=email)
    user.create()  # save the object into a database

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
