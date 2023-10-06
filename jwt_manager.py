from jwt import encode,decode

def create_token(data:dict):
    token=encode(payload=data,key="my_secret_key",algorithm="HS256")
    return token

def validate_token(token :str):
    data:dict=decode(token,key="my_secret_key",algorithm=["HS256"])