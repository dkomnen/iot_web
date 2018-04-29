from flask import Flask
from flask_restful import Resource, Api
from flask_login import LoginManager
from flask_mongoengine import MongoEngine
from flask_security import Security, MongoEngineUserDatastore
from models.UserModel import User
from models.RoleModel import Role

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
app.config['TEMPLATE_FOLDER'] = "../templates"
app.config['STATIC_FOLDER'] = "../static"
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_PASSWORD_SALT'] = "randomsalt"
app.config['SECURITY_CONFIRMABLE'] = False
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False
#app.config['SECURITY_REGISTER_USER_TEMPLATE'] = "register_user.html"


db = MongoEngine(app)
user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)


from controllers import ApiController, ViewController
