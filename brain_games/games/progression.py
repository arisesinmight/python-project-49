import random


def build_quest():
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
    question = f'{progression.replace(right_answer, "..")}'
    ask = 'What number is missing in the progression?'
    return question, right_answer, ask


if __name__ == '__main__':
    build_quest()
