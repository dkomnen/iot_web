from server import app
from flask import render_template, session
from flask_security import login_required
from models.VikingModel import Viking
from services.VikingService import VikingService
from services.UserService import UserService


@app.route("/")
# @login_required
def index():
    vikings = Viking.objects
    print vikings
    return render_template("index.html", vikings=vikings)


@app.route("/login")
def login():
    return render_template("security/login_user.html")


@app.route("/power")
@login_required
def power():
    user_id = session["user_id"]
    return render_template("power.html", user_id=user_id)


@app.route("/temperature")
@login_required
def temperature():
    user_id = session["user_id"]
    devices = UserService().get_by_user_id_and_type(user_id=user_id, device_type="temperature")
    return render_template("temperature.html", user_id=user_id, devices=devices)

