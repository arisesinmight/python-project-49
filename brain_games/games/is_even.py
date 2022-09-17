#!/usr/bin/env python3
from random import randint


def build_quest():
    question = randint(1, 100)
    if question % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    ask = 'Answer "yes" if the number is even, otherwise answer "no".'
    return question, right_answer, ask


if __name__ == '__main__':
    build_quest()
