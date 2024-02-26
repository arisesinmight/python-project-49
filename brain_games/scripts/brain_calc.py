#!/usr/bin/env python3

from brain_games.games.calculator import ask_question, build_conditions
from brain_games.engine import run_game


def brain_calc():
    run_game(ask_question, build_conditions)


if __name__ == '__main__':
    brain_calc()
