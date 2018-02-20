from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__, template_folder="../templates", static_folder="../static")
api = Api(app)

from controllers import ApiController, ViewController
