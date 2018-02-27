from BaseModel import BaseModel


class UserModel(BaseModel):

    collection_name = "user"

    def __init__(self):
        super(UserModel, self).__init__()

