#!/usr/bin/env python3

from brain_games.games.progression import build_quest
from brain_games.engine import run_game


def brain_progression():
    return run_game(build_quest)


if __name__ == '__main__':
    brain_progression()
