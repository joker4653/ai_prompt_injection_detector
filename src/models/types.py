from pydantic import BaseModel

class DetectionResult(BaseModel):
    risk: str
    score: float
    explanation: str