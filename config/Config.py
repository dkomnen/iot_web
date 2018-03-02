import importlib


class Config(object):
    config = {
        "mongo_address": "127.0.0.1",
        "mongo_port": 27017,
        "mongo_database": "heimdall",
        "mongo_user": "",
        "mongo_pass": "",
    }

    ENV_DEVELOPMENT = "dev"
    ENV_PRODUCTION = "production"
    ENV_STAGING = "staging"

    def get_config(self, key, default_value=None):
        # config_module = importlib.import_module('config.' + env)
        config_module = self.config

        return config_module[key] if key in config_module else default_value

        # @staticmethod
        # def is_env(environment):
        #     return env == environment
