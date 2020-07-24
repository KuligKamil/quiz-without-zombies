import sqlalchemy
from sqlalchemy.orm import sessionmaker

from db.models import Question, Quiz


class DAO:
    def __init__(self, database_url):
        self.engine = sqlalchemy.create_engine(database_url)
        self.engine.connect()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def get_quizzes(self, skip: int = 0, limit: int = 100):
        return self.session.query(Quiz).offset(skip).limit(limit).all()

    def get_questions(self, quiz_id):
        return self.session.query(Question).filter(Question.quiz_id == quiz_id).all()

    def close(self):
        self.session.close()
