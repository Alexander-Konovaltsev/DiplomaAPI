from pydantic import BaseModel

class GetRolesResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
