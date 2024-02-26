#!/usr/bin/env python3

from brain_games.games.is_even import ask_question, build_conditions
from brain_games.engine import run_game


def brain_even():
    run_game(ask_question, build_conditions)


if __name__ == '__main__':
    brain_even()
