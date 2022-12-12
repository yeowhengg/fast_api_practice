from pydantic import BaseModel
from typing import Optional
from sqlmodel import Field

class AddArtifects(BaseModel):
    name: str
    element: str
    level: int

    class Config:
        orm_mode = True
        
class GenshinItem(BaseModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    element: str
    level: int

    # arbitrary class instances that helps models to be mapped to ORM objects
    # e.g. use case: it will try to retrieve the data by using a dict or directly from the model attribute (genshin.name)
    class Config:
        orm_mode = True

class UpdateItem(BaseModel):
    name: str
    level: int

    class Config:
        orm_mode = True