from pydantic import BaseModel
from typing import Optional
from schemas.question_type import QuestionTypeResponse

class QuestionResponse(BaseModel):
    id: int
    question_text: str
    quiz_id: int
    model_id: Optional[int]
    question_type_id: int
    question_type: QuestionTypeResponse

    class Config:
        from_attributes = True
