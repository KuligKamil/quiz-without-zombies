import requests
import yaml
import sqlalchemy

from sqlalchemy.orm import sessionmaker

from db.models import Quiz, Question, Answer
from env import URL

print(URL)


def get_questions_from_api():
    questions = []
    data = requests.get('https://opentdb.com/api.php?amount=5&category=27&difficulty=easy&type=multiple').json()
    print(data['results'])
    for i in data['results']:
        answers = [{'name': x} for x in i['incorrect_answers']]
        answers.append({'name': i['correct_answer'], 'is_correct': True})
        print(i['question'])
        print(i['incorrect_answers'])
        print(i['correct_answer'])
        print()
        question = {
            'name': i['question'],
            'answers': answers
        }
        questions.append(question)
    return questions


def get_questions_from_yml(name_file):
    questions = []
    with open(name_file, 'r') as stream:
        try:
            questions = yaml.safe_load(stream)
            print(yaml.safe_load(stream))
        except yaml.YAMLError as e:
            print(e)
    return questions


def get_questions_from_db():
    engine = sqlalchemy.create_engine(URL)
    engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()
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

    print(answers)
    print(len(answers))
    print(type(answers))

    print(questions)
    print(len(questions))
    print(type(questions))

    for question in questions:
        question['answers'] = []
        for answer in answers:
            if question['id'] == answer['question_id']:
                question['answers'].append(answer)

    print(questions)
    session.close()
    return questions
