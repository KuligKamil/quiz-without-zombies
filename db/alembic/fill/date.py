from sqlalchemy.orm.session import Session

from data import get_questions_from_yml
from db.models import Quiz, Question, Answer


def fill_db(op):
    session = Session(bind=op.get_bind())
    is_exist = bool(session.query(Quiz) \
                    .filter(Quiz.name == 'First quiz') \
                    .first())
    print(is_exist)
    if is_exist is False:
        questions = get_questions_from_yml('data.yml')
        quiz = Quiz(name='First quiz')
        session.add(quiz)
        for question in questions:
            new_question = Question(name=question['name'], quiz=quiz)
            session.add(new_question)
            for answer in question['answers']:
                if 'is_correct' in answer:
                    new_answer = Answer(name=answer['name'], is_correct=answer['is_correct'], question=new_question)
                else:
                    new_answer = Answer(name=answer['name'], is_correct=False, question=new_question)
                session.add(new_answer)
        session.commit()

    questions = session.query(Question.name,
                              Question.id) \
        .filter(Question.quiz_id == 1) \
        .all()

    answers = session.query(Answer.name,
                            Answer.is_correct,
                            Answer.question_id) \
        .join(Question) \
        .filter(Question.quiz_id == 1) \
        .all()

    answers = [i._asdict() for i in answers]
    questions = [i._asdict() for i in questions]

    for question in questions:
        question['answers'] = []
        for answer in answers:
            if question['id'] == answer['question_id']:
                question['answers'].append(answer)

    session.close()
