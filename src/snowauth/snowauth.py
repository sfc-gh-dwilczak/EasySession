import toml
from snowflake.snowpark.session import Session


def connect(file_name,header):
    with open(file_name, 'r') as f:
        creds = toml.load(f)

    if not creds:
        raise Exception('Connection Name not Found!')
    
    return Session.builder.configs(creds[header]).create()