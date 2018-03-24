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
        start_timestamp = data['start_timestamp']
        end_timestamp = data['end_timestamp']

        # return self.model(payload=unit).save().to_json()
        return self.model(serial_number=serial_number, temperature=temperature, unit=unit,
                          start_timestamp=start_timestamp, end_timestamp=end_timestamp).save().to_json()
