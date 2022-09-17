#!/usr/bin/env python3

from brain_games.games.is_even import build_quest
from brain_games.engine import run_game


def brain_even():
    return run_game(build_quest)


if __name__ == '__main__':
    brain_even()
