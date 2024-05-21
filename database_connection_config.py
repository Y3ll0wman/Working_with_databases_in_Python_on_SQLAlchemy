import json

from pydantic import BaseModel


class DataBaseConnectionDetails(BaseModel):
    login: str
    password: str
    host: str
    port: str
    db_name: str


def open_config():
    config_path = 'database_connection_config.json'

    with open(config_path) as json_file:
        config = json.load(json_file)

    return config


data = open_config()

database_connection_config = DataBaseConnectionDetails(**data)


class DataBaseConnectionsConfig:
    login = database_connection_config.login
    password = database_connection_config.password
    host = database_connection_config.host
    port = database_connection_config.port
    db_name = database_connection_config.db_name


db_config = DataBaseConnectionsConfig()
