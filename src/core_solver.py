from typing import Set, Optional, Callable, List
import functools
import time
from visualizer import visualize

RESTRICT_WORD_LENGTH = True


def is_levenshtein_distance_one(w1: str, w2: str) -> bool:
    lw1, lw2 = len(w1), len(w2)
    if lw1 == lw2:
        changes = sum(1 for i in range(lw1) if w1[i] != w2[i])
        return changes == 1
    elif RESTRICT_WORD_LENGTH and lw1 - lw2 == 1:
        return w2 in w1
    elif RESTRICT_WORD_LENGTH and lw2 - lw1 == 1:
        return w1 in w2
    return False


def get_neighbours_by_vocabulary_factory(
    vocabulary: Set[str],
) -> Callable[[str], Set[str]]:
    @functools.cache
    def get_neighbours(w):
        return {hw for hw in vocabulary if is_levenshtein_distance_one(w, hw)}

    return get_neighbours


def find_path_bfs(
    src: str, dst: str, get_neighbours_f: Callable[[str], Set[str]]
) -> Optional[List[str]]:
    visited = set()
    queue_of_paths = [[src]]
    while len(queue_of_paths) > 0:
        path = queue_of_paths.pop(0)
        node = path[-1]
        if node == dst:
            return path
        visited.add(node)
        neighbours = get_neighbours_f(node)
        queue_of_paths.extend([path + [e] for e in neighbours.difference(visited)])
    return None


def find_shortest_words_path(start: str, end: str, vocabulary: Set[str]) -> None:
    begin = time.time()
    if any(e not in vocabulary for e in [start, end]):
        print("Unrecognized... Aborting.")
    if RESTRICT_WORD_LENGTH:
        assert len(start) == len(end)
        restricted_vocabulary = {w for w in vocabulary if len(w) == len(start)}
        neighbours_func = get_neighbours_by_vocabulary_factory(restricted_vocabulary)
    else:
        neighbours_func = get_neighbours_by_vocabulary_factory(vocabulary)
    path = find_path_bfs(start, end, neighbours_func)
    if path is None:
        print("Sorry! No path found.")
    else:
        # print(' ,'.join([e[::-1] for e in path]))   # terminal printing...
        print(f"Found path:\n{path}")
    print(f"\t(Took {(time.time() - begin):.2f} seconds to compute)")
    visualize(path, neighbours_func)
