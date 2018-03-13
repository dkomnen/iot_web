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
        timestamp = data['timestamp']


        #return self.model(payload=unit).save().to_json()
        return self.model(serial_number=serial_number, temperature=temperature, unit=unit, timestamp=timestamp).save().to_json()
