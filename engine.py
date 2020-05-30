import string
import yaml
from get_data import get_questions_from_api

with open("data.yml", 'r') as stream:
    try:
        questions = yaml.safe_load(stream)
        print(yaml.safe_load(stream))
    except yaml.YAMLError as e:
        print(e)
questions = questions + get_questions_from_api()
print(questions)
print(len(questions))


def clear(num):
    for _ in range(num):
        print()


signs = string.ascii_uppercase[:4]
points = 0

clear(80)
for index, question in enumerate(questions):
    print(question['content'])
    for i, answer in enumerate(question['answers']):
        print(signs[i], answer['content'])

    is_answer_not_ok = True
    while is_answer_not_ok:
        answer = input("Please enter sign answer: ")
        print("You entered: " + answer)
        if answer in signs:
            is_answer_not_ok = False
    helper = -1
    for i, sign in enumerate(signs):
        if sign == answer:
            helper = i
    print(question['answers'][helper]['content'])
    if 'is_correct' in question['answers'][helper]:
        print('Good answer')
        points += 1
    else:
        print('Wrong answer')
    if index == len(questions) - 1:
        input("Please enter to get result")
    else:
        input("Please enter to get next question")
    clear(80)

print('Result: ', points, '/ ', len(questions))
