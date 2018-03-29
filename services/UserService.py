from services.BaseService import BaseService
from models.UserModel import User


class UserService(BaseService):

    def __init__(self):
        super(UserService, self).__init__()
        self.model = User

