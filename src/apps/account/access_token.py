import uuid

class AccessToken:

    def __init__(self,device_id) -> None:
        self.did = device_id

    def __repr__(self) -> str:
        return "{0}{1}".format(self.did,str(uuid.uuid4().hex))    