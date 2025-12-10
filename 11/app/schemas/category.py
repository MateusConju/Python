from pydantic import BaseModel, Field

class CategoryCreate(BaseModel):
    name:str = Field(..., max_length=50)
    slug:str = Field(..., max_length=50)

class CategoryResponse(BaseModel):
    id:int
    name:str
    slug:str
    class Config:
        from_attributes = True
