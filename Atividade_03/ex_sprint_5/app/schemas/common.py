from typing import Generic, TypeVar, Optional, Dict, Any
from pydantic import BaseModel

T = TypeVar("T")


class StandardResponse(BaseModel, Generic[T]):
    """
    Envelope Genérico
    -----------------
    - success: bool
    - message: str
    - data: Optional[T]
    - meta: dict opcional
    """

    success: bool
    message: str
    data: Optional[T] = None
    meta: Optional[Dict[str, Any]] = None
