import random


ask_question = 'Find the greatest common divisor of given numbers.'


def find_gsd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def build_conditions():
    question = f'{random.randint(1, 100)} {random.randint(1, 100)}'
    indexed_question = question.partition(' ')
    a = int(indexed_question[0])
    b = int(indexed_question[2])
    right_answer = str(find_gsd(a, b))
    return question, right_answer
