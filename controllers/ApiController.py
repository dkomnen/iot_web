from server import api
from flask_restful import Resource, request
from models.VikingModel import Viking


class HelloWorld(Resource):
    def get(self):
        #return {'hello': 'world'}
        print Viking().get_all()
        return Viking().get_all()

    def post(self, data):
        request_data = request.get_json()
        return Viking().create(request_data)

api.add_resource(HelloWorld, '/test')
