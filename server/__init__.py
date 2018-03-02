from flask import Flask
from flask_restful import Resource, Api
from flask_login import LoginManager
from flask_mongoengine import MongoEngine

app = Flask(__name__, template_folder="../templates", static_folder="../static")
api = Api(app)

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

app.config['MONGODB_SETTINGS'] = {
    "db": "heimdall",
    "username":"",
    "password":"",
    "host": "127.0.0.1",
    "port": 27017

}
db = MongoEngine(app)


from controllers import ApiController, ViewController
