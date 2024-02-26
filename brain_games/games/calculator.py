import random


ask_question = 'What is the result of the expression?'


def build_conditions():
    operator = ["+", "-", "*"]
    question = f'{random.randint(1, 100)} \
{random.choice(operator)} {random.randint(1, 100)}'
    right_answer = str(eval(question))
    return question, right_answer
