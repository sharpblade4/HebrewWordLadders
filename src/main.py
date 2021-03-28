#!/usr/bin/env python3
import sys
from core_solver import find_shortest_words_path
from vocabulary_provider import get_hebrew_vocabulary


def _run(w1: str, w2: str) -> None:
    find_shortest_words_path(w1, w2, get_hebrew_vocabulary())


def _test():
    _run("עבדות", "חירות")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            "Incorrect usage. Supply two words to the runner. E.g. `./src/main.py עבדות חירות`"
        )
        exit(-1)
    _run(sys.argv[1], sys.argv[2])
