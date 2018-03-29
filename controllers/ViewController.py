from server import app
from flask import render_template
from flask_security import login_required
from models.VikingModel import Viking


@app.route("/")
# @login_required
def index():
    vikings = Viking.objects
    print vikings
    return render_template("index.html", vikings=vikings)


@app.route("/login")
def login():
    return render_template("security/login_user.html")


    # @app.route('/register', methods=['GET', 'POST'])
    # def register_test():
    #     return render_template("security/register_user.html")
