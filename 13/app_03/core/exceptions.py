
class ResourceNotFoundException(Exception):
    def __init__(self, resource:str, id:int):
        self.resource = resource
        self.id = id