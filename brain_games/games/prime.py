import random


ask_question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for i in range(2, ((int(number)) // 2) + 1):
        if (int(number)) % i == 0:
            return False
    return True


def build_conditions():
    question = f'{random.randint(1, 100)}'
    if is_prime(question):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer
