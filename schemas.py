from typing import List
from pydantic import BaseModel


class Quiz(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class Answer(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class Question(BaseModel):
    id: int
    name: str
    answers: List[Answer] = []

    class Config:
        orm_mode = True
