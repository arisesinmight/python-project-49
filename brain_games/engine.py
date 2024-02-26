import prompt


ROUNDS_TO_WIN = 3


def run_game(ask_question, build_conditions):
    print("Welcome to the Brain Games!")
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!\n{ask_question}')
    counter = 0
    while counter < ROUNDS_TO_WIN:
        question, right_answer = build_conditions()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != right_answer:
            print(f'"{answer}" is wrong answer ;(. \
Correct answer was "{right_answer}".\n\
Let\'s try again, {username}!')
            return
        else:
            print('Correct!')
            counter += 1
    print(f"Congratulations, {username}!")
    return
