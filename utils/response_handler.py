from flask import Response
import json


class ResponseHandler(object):

    STATUS_OK = 200
    STATUS_CREATED = 201

    STATUS_BAD_REQUEST = 400
    STATUS_UNAUTHORIZED_REQUEST = 401
    STATUS_FORBIDDEN = 403
    STATUS_NOT_FOUND = 404
    STATUS_METHOD_NOT_ALLOWED = 405

    STATUS_UNPROCESSABLE_REQUEST = 422

    STATUS_INTERNAL_SERVER_ERROR = 500
    STATUS_BAD_GATEWAY = 502

    def __init__(self):
        pass

    @staticmethod
    def success(response_data, response_status=STATUS_OK):
        resp = Response(response=json.dumps(response_data), status=response_status, mimetype='application/json')
        resp.headers['Access-Control-Allow-Origin'] = '*'

        return resp

    @staticmethod
    def fail(message, response_status, data={}):
        resp = Response(
            response=json.dumps({
                "message": message,
                "data": data,
                "status": response_status
            }),
            status=response_status,
            mimetype='application/json'
        )
        return resp

    # def not_found_response(self):
    def response_created(self, data):
        return self.success(data)

    def bad_request(self, message, data={}):
        return self.fail(message, self.STATUS_BAD_REQUEST, data)

    def unauthorized_request(self, message, data={}):
        return self.fail(message, self.STATUS_UNAUTHORIZED_REQUEST, data)

    def forbidden(self, message, data={}):
        return self.fail(message, self.STATUS_FORBIDDEN, data)

    def not_found(self, message, data={}):
        return self.fail(message, self.STATUS_NOT_FOUND, data)

    def method_not_allowed(self, message, data={}):
        return self.fail(message, self.STATUS_METHOD_NOT_ALLOWED, data)

    def internal_server_error(self, message, data={}):
        return self.fail(message, self.STATUS_INTERNAL_SERVER_ERROR, data)

    def bad_gateway(self, message, data={}):
        return self.fail(message, self.STATUS_BAD_GATEWAY, data)

    def unprocessable_request(self, message, data={}):
        return self.fail(message, self.STATUS_UNPROCESSABLE_REQUEST, data)

response_handler = ResponseHandler()
