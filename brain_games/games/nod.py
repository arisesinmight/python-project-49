import random
import math


def build_quest():
    question = f'{random.randint(1, 100)} {random.randint(1, 100)}'
    indexed_question = question.partition(' ')
    a = int(indexed_question[0])
    b = int(indexed_question[2])
    right_answer = str(math.gcd(a, b))
    ask = 'Find the greatest common divisor of given numbers.'
    return question, right_answer, ask


if __name__ == '__main__':
    build_quest()
