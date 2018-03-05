from services.BaseService import BaseService
from models.VikingModel import Viking


class VikingService(BaseService):

    def __init__(self):
        super(VikingService, self).__init__()
        self.model = Viking

    def create(self, data):
        serial_number = data['serial_number']
        temperature = data['temperature']
        unit = data['unit']

        #return self.model(payload=unit).save().to_json()
        return self.model(serial_number=serial_number, temperature=temperature, unit=unit).save().to_json()
