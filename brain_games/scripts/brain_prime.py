#!/usr/bin/env python3

from brain_games.games.prime import ask_question, build_conditions
from brain_games.engine import run_game


def brain_prime():
    run_game(ask_question, build_conditions)


if __name__ == '__main__':
    brain_prime()
