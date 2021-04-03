#!/usr/bin/env python3
# Bonus activity, unrelated to hebrew word ladders - the monty hall problem.

 import random
 from typing import Optional, List
 
 def _remove(l: List[int], e: int) -> List[int]:
    l.remove(e)
    return l
 
 def play_game(verbose: bool = False, strategy_replace: Optional[bool] = None) -> bool:
    car = random.choice([1,2,3])
    choose_1 = random.choice([1,2,3])
    if choose_1 == car:
        goat = random.choice(_remove([1,2,3], car))
    else:
        goat = _remove(_remove([1,2,3], car), choose_1)[0]
    if strategy_replace is None:
        strategy_replace = random.choice([True, False])
    if strategy_replace:
        choose_2 = _remove(_remove([1,2,3], choose_1), goat)[0]
    else:
        choose_2 = choose_1
    win = choose_2 == car
    if verbose:
      print("\t"*(car-1)+"C\n_\t_\t_")
      print("\t"*(choose_1-1)+"^")
      print("\t"*(goat-1)+"X")
      print("\t"*(choose_2-1)+"^")
      print("Won a car!" if win else "Got a goat.")
    return win
        
 def main() -> None:
    n=1000000
    replace_wins = sum([1 if play_game(True) else 0 for i in range(n)])
    stick_wins = sum([1 if play_game(False) else 0 for i in range(n)])
    random_wins = sum([1 if play_game() else 0 for i in range(n)])
    print(f"Replace: {replace_wins/n}, Stick:{stick_wins/n}, Random: {random_wins/n}")
 
