from server import api
from flask import request, Response
from flask_restful import Resource
from utils.response_handler import response_handler

from models.VikingModel import Viking


class HelloWorld(Resource):
    def get(self):
        return response_handler.success(response_data=Viking().get_all())

    def post(self):
        request_data = request.get_json()
        return response_handler.success(respone_data=Viking().create(request_data))

api.add_resource(HelloWorld, '/test')
