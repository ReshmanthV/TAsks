from configparser import ConfigParser

config = ConfigParser()
config.read("conf/application.conf")


class Service:
    port = int(config["SERVICE"]["port"])
    host = config["SERVICE"]["host"]
    uri = config["MONGO_DB"]["uri"]


class Authentication:
    sender_mail = config["SENDER_MAIL"]['sender']
    sender_password = config["SENDER_MAIL"]['password']

