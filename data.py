import requests
import yaml


def get_questions_from_api():
    questions = []
    data = requests.get('https://opentdb.com/api.php?amount=5&category=27&difficulty=easy&type=multiple').json()
    print(data['results'])
    for i in data['results']:
        answers = [{'content': x} for x in i['incorrect_answers']]
        answers.append({'content': i['correct_answer'], 'is_correct': True})
        print(i['question'])
        print(i['incorrect_answers'])
        print(i['correct_answer'])
        print()
        question = {
            'content': i['question'],
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
