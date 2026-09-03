# Two pointers is the act of using two pointers or indices to move through a structure at a time.
# Usually these are done to avoid using nested loops or repeating indices.
# One pointer tracks the start and the other the end.
# There are two types, pointers moving together in the same directions. And the pointers moving towards eachother from opposite directions.

## Same direction patterns show up when doing a single pass over the data but you need to track a range and not one element at the same time.
# A common setup is the fast and slow pointer, where ones moves one step at a time, while another might move two.
# What this allows you to do is detect patterns in a single pass.

# For example, while one reaches the end and the other is halfway then you have found the middle. If one laps the slow pointer then youve detected
# a cycle.

# For opposite direction patterns one starts at the start and the other at the end and move inward.

# Youll see these when the array is sorted and your trying to find a pair or combination or comparing symmetric parts of a structure.
# Checking for palindromes, avoiding nested loops when checking all pairs.

# Move one pointer at a time, check, then move the other. Check again, and etc.

# Instead of checking all combinations, O(N^2) this allows you to check in O(n).

# Two pointers:
## 1. Reduces the number of iterations you need.
## 2. Tracks a relationship between two places.
## 3. Avoid extra space by not needing sets or maps.
## This optimizes time and space complexity at once.

# Two pointers come up in problems involving palindromes, reversals, merging sorted data, and k sized comparisons.

# Ask can you do this in one pass, if yes (then you should be using two pointers.)

