import random


def build_quest():
    ask = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    question = f'{random.randint(1, 100)}'
    right_answer = 'yes'
    for i in range(2, ((int(question)) // 2) + 1):
        if (int(question)) % i == 0:
            right_answer = 'no'
    return question, right_answer, ask


if __name__ == '__main__':
    build_quest()
