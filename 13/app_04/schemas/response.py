from typing import Generic, TypeVar,  Optional
from pydantic import BaseModel

T = TypeVar('T')

class ResponseEnvelope(BaseModel, Generic[T]):
    data:Optional[T]
    message:str = "Success"
    success:bool = True
    meta:dict = {}
    