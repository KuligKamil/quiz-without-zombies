from typing import List
import uvicorn
from fastapi import FastAPI

from settings import DATABASE_URL_DOCKER
import schemas
from dao import DAO

app = FastAPI()
dao = DAO(DATABASE_URL_DOCKER)


def get_db():
    dao = DAO(DATABASE_URL_DOCKER)
    try:
        yield dao
    finally:
        dao.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/quizzes/", response_model=List[schemas.Quiz])
def get_quizzes():
    return dao.get_quizzes()


@app.get("/quizzes/{quiz_id}/questions/", response_model=List[schemas.Question])
def get_questions(quiz_id):
    return dao.get_questions(quiz_id=quiz_id)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
