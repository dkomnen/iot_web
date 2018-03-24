from mongoengine import Document


class BaseModel(Document):
    collection_name = None
