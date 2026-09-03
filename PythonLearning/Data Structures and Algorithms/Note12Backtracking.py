# Backtracking is a recursive problem solving technique that explores all possible configurations of a solution but efficiently
# Backs up when it realizes a path will not work.

# If your solving a puzzle and you realize something wont work you undo it, backtracking is the same way.

# DFS With the ability to reverse a choice.

# Use backtracking when...
# 1. The solution involves Combinations, permutations, etc...
# 2. Building up a partial solution one step at a time.
# 3. Want all possible solutions or the first valid one.
# 4. Need to discard bad paths early.

# Backtracking formula.

def backtrack(path, choices):
    # base case
    if goal_reached(path):
        result.append(path.copy())
        return

    for choice in choices:
        if not valid(choice, path):
            continue

        # choose
        path.append(choice)

        # explore
        backtrack(path, choices)

        # undo choice
        path.pop()

# How to spot a backtracking problem
# 1. Generate all combinations or arrangements.
# 2. Building up a partial solution.
# 3. Want all possible solutions
# 4. Need to discard bad paths early.
