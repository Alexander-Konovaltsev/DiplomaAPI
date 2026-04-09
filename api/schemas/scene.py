from pydantic import BaseModel

class SceneResponse(BaseModel):
    id: int
    name: str
    title: str
    description: str

    class Config:
        from_attributes = True
        