from pydantic import BaseModel
from typing import Optional

class ModelResponse(BaseModel):
    id: int
    name: str
    title: str
    description: Optional[str]
    is_draggable: bool
    is_rotatable: bool
    is_assemblable: bool
    is_informational: bool
    parent_id: Optional[int]

    class Config:
        from_attributes = True
