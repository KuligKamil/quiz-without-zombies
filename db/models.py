from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, func, DateTime
from sqlalchemy.orm import relationship

Base = declarative_base()


class Time:
    created = Column(DateTime, server_default=func.now())
    modified = Column(DateTime, server_default=func.now(), onupdate=func.now())


class Quiz(Base, Time):
    name = Column(String)
    question = relationship("Question", backref="parent")

    def __init__(self, name):
        self.name = name


class Question(Base, Time):
    name = Column(String)
    quiz_id = Column(Integer, ForeignKey('quiz.id'))
    answer = relationship("Answer", backref="parent")
    quiz = relationship("Quiz", backref="child")

    def __init__(self, name, quiz):
        self.name = name
        self.quiz = quiz


class Answer(Base, Time):
    name = Column(String)
    is_correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey('question.id'))
    question = relationship("Question", backref="child")

    def __init__(self, name, is_correct, question):
        self.name = name
        self.is_correct = is_correct
        self.question = question
