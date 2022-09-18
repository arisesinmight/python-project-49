import random
import sympy


def build_quest():
    ask = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    random_number = {random.randint(1, 100)
    question = random_number
    if sympy.isprime(int(question)) is True:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer, ask


if __name__ == '__main__':
    build_quest()
