import importlib


class Config(object):
    config = {

        # "base_web_url": "http://192.168.69.70:4444",
        # "base_api_url": "http://192.168.69.96:4445",
        # "appstore_url": "http://www.distribooted.com/appstore.html",

        "mongo_address": "159.100.250.251",
        "mongo_database": "distribooted",
        "mongo_user": "dstrbtd",
        "mongo_pass": "dstrbtdpas$",
    }

    ENV_DEVELOPMENT = "dev"
    ENV_PRODUCTION = "production"
    ENV_STAGING = "staging"

    def get_config(self, key, default_value=None):
        # config_module = importlib.import_module('config.' + env)
        config_module = self.config

        return config_module.config[key] if key in config_module.config else default_value

        # @staticmethod
        # def is_env(environment):
        #     return env == environment
