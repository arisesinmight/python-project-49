import random


ask_question = 'What number is missing in the progression?'


def build_conditions():
    start = random.randint(0, 50)
    step = random.randint(2, 10)
    lenght = random.randint(5, 10)
    progression = f'{start}'
    counter = 0
    while counter < lenght - 1:
        progression += (' ' + str(start + step))
        start += step
        counter += 1
    progression_tuple = progression.split(' ')
    right_answer = random.choice(progression_tuple)
    hidden_question = progression.replace(right_answer, "..")
    question = f'{hidden_question}'
    return question, right_answer
