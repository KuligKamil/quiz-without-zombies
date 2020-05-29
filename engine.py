import string


def clear(num):
    for _ in range(num):
        print()


questions = [{
    'content': 'Which team won the 2018 World Cup?',
    'answers': [
        {'content': 'French', 'is_correct': True},
        {'content': 'England'},
        {'content': 'Spain'},
        {'content': 'Croatia'}
    ]
}, {
    'content': 'Which team won Europe Cup in 2016?',
    'answers': [
        {'content': 'Portugal ', 'is_correct': True},
        {'content': 'Poland'},
        {'content': 'Russia'},
        {'content': 'French'}
    ]
},
    {'content': 'Won Champion League in 2012?',
     'answers': [
         {'content': 'Bayern Munich'},
         {'content': 'Real Madryt'},
         {'content': 'Manchester United'},
         {'content': 'Chelsea F.C.', 'is_correct': True}
     ]}
]
clear(80)
signs = string.ascii_uppercase[:4]
for question in questions:
    print(question['content'])
    for i, answer in enumerate(question['answers']):
        print(signs[i], answer['content'])

    answer = input("Please enter sign answer: ")
    print("You entered: " + answer)
    helper = -1
    for i, sign in enumerate(signs):
        if sign == answer:
            helper = i
    print(question['answers'][helper]['content'])
    if 'is_correct' in question['answers'][helper]:
        print('Good answer')
    else:
        print('Wrong answer')
    input("Please enter to get next question")
    clear(80)
