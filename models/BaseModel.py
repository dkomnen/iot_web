from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
import datetime
from config.Config import Config


class BaseModel(object):

    db_name = "heimdall"
    collection_name = None

    def __init__(self):
        self.collection = ""

        self.db_name = Config().get_config("mongo_database")
        self.host = Config().get_config("mongo_address")
        self.mongo_user = Config().get_config("mongo_user")
        self.mongo_pass = Config().get_config("mongo_pass")

        self.client = MongoClient(self.host)
        self.db = self.client[self.db_name]

        #self.db.authenticate(self.mongo_user, self.mongo_pass)

        self.collection = self.db[self.collection_name]

    def create(self, data):
        data["created_at"] = datetime.datetime.now()
        cr_obj = self.collection.insert_one(data)
        obj = self.find_by_id(cr_obj.inserted_id)
        return obj

    def get_all(self):
        return self.as_dict(self.find({}))

    def find(self, condition, skip=0, limit=0):
        return self.collection.find(condition, skip=skip, limit=limit)

    def find_one(self, condition):
        return self.collection.find_one(condition)

    def find_by_id(self, id):
        return self.collection.find_one({'_id': ObjectId(id)})

    def find_where_in(self, key, values):
        return self.collection.find({key: {"$in": values}})

    def find_or_create(self, condition, data=None):
        cursor = self.find(condition)

        if cursor.count() == 0:
            if not data:
                data = condition

            obj = self.create(data)
        else:
            obj = cursor[0]

        return obj

    def update(self, id_or_where, key, value):

        if not isinstance(id_or_where, (dict)):
            id_or_where = {"_id": ObjectId(id_or_where)}

        self.collection.update_one(
            id_or_where,
            {
                '$set': {key: value}
            }
        )
        self.updated_at(id_or_where)

    def update_where(self, condition, data):

        self.collection.update(
            condition,
            {
                '$set': data
            }
        )
        # self.updated_at(id)

    def updated_at(self, id_or_where):

        if not isinstance(id_or_where, (dict)):
            id_or_where = {"_id": ObjectId(id_or_where)}

        self.collection.update_one(
            id_or_where,
            {
                '$set': {"updated_at": datetime.datetime.now()}
            }
        )

    def add_item(self, id_or_where, field, value):

        if not isinstance(id_or_where, (dict)):
            id_or_where = {"_id": ObjectId(id_or_where)}

        self.collection.update(
            id_or_where,
            {'$addToSet': {field: value}}
        )

    def remove(self, id_or_where, key):

        if not isinstance(id_or_where, (dict)):
            id_or_where = {"_id": ObjectId(id_or_where)}

        self.collection.update_one(
            id_or_where,
            {
                '$unset': {key: 1}
            }
        )
        self.updated_at(id_or_where)

    def generate_id(self):
        return ObjectId()

    def count(self, condition):
        return self.collection.count(condition)

    def inc(self, condition_or_id, field, amount=1):
        condition = condition_or_id

        if not isinstance(condition_or_id, (dict, list)):
            condition = {"_id": ObjectId(condition_or_id)}

        return self.collection.update(condition, {'$inc': {field: amount}})

    def as_dict(self, data):
        return dumps(data)
