#!/usr/bin/env python3
from random import randint
import prompt

print("Welcome to the Brain Games!")

name = prompt.string('May I have your name? ')
print(f'Hello, {name}!')

print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even():
    counter = 0
    while counter < 3:
        number = randint(1, 100)
        print(f'Question: {number}')
        if number % 2 == 0:
            right_answer = 'yes'
            answer = input()
            if answer != right_answer:
                print(f'"no" is wrong answer ;(. Correct answer was "yes".\n\
                    Let\'s try again, {name}!')
                return
            else:
                print('Correct!')
                counter += 1
        else:
            right_answer = 'no'
            answer = input()
            if answer != right_answer:
                print(f'"yes" is wrong answer ;(. Correct answer was "no".\n\
                    Let\'s try again, {name}!')
                return
            else:
                print('Correct!')
                counter += 1

    print(f"Congratulations, {name}")
    return


if __name__ == '__main__':
    is_even()
