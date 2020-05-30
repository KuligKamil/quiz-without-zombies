import string
import random
import time
from data import get_questions_from_yml, get_questions_from_api

TIME_LIMIT = 15
time_total = 0
signs = string.ascii_uppercase[:4]
points = 0
questions = get_questions_from_yml('data.yml') + get_questions_from_api()

random.shuffle(questions)
for question in questions:
    random.shuffle(question['answers'])


def clear(num):
    for _ in range(num):
        print()


clear(80)
for index, question in enumerate(questions):
    print(question['content'])
    for i, answer in enumerate(question['answers']):
        print(signs[i], answer['content'])
    time_start = time.time()
    time_elapsed = 0
    is_answer_not_ok = True
    while is_answer_not_ok and time_elapsed < TIME_LIMIT:
        answer = input('Please enter sign answer: ')
        print(f'You entered: {answer}')
        if answer in signs:
            is_answer_not_ok = False

    time_elapsed = time.time() - time_start
    time_total += time_elapsed
    if time_elapsed > TIME_LIMIT:
        print(f'Too late, {int(time_elapsed)} sek')
    else:
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
    print(f'Answer time: {int(time_elapsed)} sek')
    if index == len(questions) - 1:
        input('Please enter to get result')
    else:
        input('Please enter to get next question')
    clear(80)

print(f'Result: {points} / {len(questions)}')
print(f'Total time: {int(time_total)} sek')
