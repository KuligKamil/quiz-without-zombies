from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Quiz(Base):
    __tablename__ = 'quiz'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    question = relationship("Question", backref="parent")

    def __init__(self, name):
        self.name = name


class Question(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    quiz_id = Column(Integer, ForeignKey('quiz.id'))
    answer = relationship("Answer", backref="parent")
    quiz = relationship("Quiz", backref="child")

    def __init__(self, name, quiz):
        self.name = name
        self.quiz = quiz


class Answer(Base):
    __tablename__ = 'answer'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    is_correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey('question.id'))
    question = relationship("Question", backref="child")

    def __init__(self, name, is_correct, question):
        self.name = name
        self.is_correct = is_correct
        self.question = question
