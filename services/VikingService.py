from services.BaseService import BaseService
from models.VikingModel import Viking


class VikingService(BaseService):

    def __init__(self):
        super(VikingService, self).__init__()
        self.model = Viking