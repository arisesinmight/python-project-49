import random


def build_quest():
    operator = ["+", "-", "*"]
    question = f'{random.randint(1, 100)} \
{random.choice(operator)} {random.randint(1, 100)}'
    right_answer = str(eval(question))
    ask = 'What is the result of the expression?'
    return question, right_answer, ask


if __name__ == '__main__':
    build_quest()
