from server import app
from flask import render_template
from flask_security import login_required


@app.route("/")
#@login_required
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("security/login_user.html")


# @app.route('/register', methods=['GET', 'POST'])
# def register_test():
#     return render_template("security/register_user.html")