from pydantic import BaseModel

class QuizResponse(BaseModel):
    id: int
    title: str
    description: str
    attempts_count: int
    questions_count: int
    time: int
    scene_id: int

    class Config:
        from_attributes = True
