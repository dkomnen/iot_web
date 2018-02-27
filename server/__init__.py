from flask import Flask
from flask_restful import Resource, Api
from flask_login import LoginManager

app = Flask(__name__, template_folder="../templates", static_folder="../static")
login_manager = LoginManager()
api = Api(app)
login_manager.login_view = "login"
login_manager.init_app(app)

from controllers import ApiController, ViewController
