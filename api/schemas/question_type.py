from pydantic import BaseModel

class QuestionTypeResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
        