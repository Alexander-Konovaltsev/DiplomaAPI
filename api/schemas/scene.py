from pydantic import BaseModel

class SceneResponse(BaseModel):
    id: int
    name: str
    title: str
    descripiton: str

    class Config:
        from_attributes = True
        