import prompt


def run_game(build_quest):
    print("Welcome to the Brain Games!")
    username = prompt.string('May I have your name? ')
    question, right_answer, ask = build_quest()
    print(f'Hello, {username}!\n{ask}')
    counter = 0
    while counter < 3:
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
            question, right_answer, ask = build_quest()
    print(f"Congratulations, {username}!")
    return


if __name__ == '__main__':
    run_game()
