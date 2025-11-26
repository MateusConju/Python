from typing import Annotated
from fastapi import Depends

def pagination_params(page: int = 1, limit: int = 10) -> dict[str, int]:
    return {"page": page, "limit": limit}

def get_query_filter(q:str | None = None, pagination:dict = Depends(pagination_params)):
    return {
        "filter":q,
        "offset":pagination["skip"],
        "max":pagination["limit"]
    }
PaginationDep = Annotated[dict[str, int], Depends(pagination_params)]
