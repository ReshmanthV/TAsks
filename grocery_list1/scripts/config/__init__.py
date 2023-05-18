from configparser import ConfigParser

config = ConfigParser()
config.read("conf/application.conf")


class Service:
    port = int(config["SERVICE"]["port"])
    host = config["SERVICE"]["host"]
    uri = config["MONGO_DB"]["uri"]
    database_name = config["MONGO_DB"]["database_name"]
    collection_name = config["MONGO_DB"]["collection_name"]


class Authentication:
    sender_mail = config["SENDER_MAIL"]['sender']
    sender_password = config["SENDER_MAIL"]['password']

