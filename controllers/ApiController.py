from server import api
from flask_restful import Resource
from models.VikingModel import Viking


class HelloWorld(Resource):
    def get(self):
        #return {'hello': 'world'}
        print Viking().get_all()
        return Viking().get_all()

    def post(self):
        return {'hello': 'world_post'}

api.add_resource(HelloWorld, '/test')
