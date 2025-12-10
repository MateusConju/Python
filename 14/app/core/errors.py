from fastapi import HTTPException

class StatusCodeNotFound(HTTPException):
    def __init__(self, detail = None, headers = None):
        super().__init__(404, detail, headers)