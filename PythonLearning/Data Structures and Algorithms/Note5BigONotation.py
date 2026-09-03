## Big O Notation.

## Big O Notation talks about how long it will take your solution to run.

# O(n!) - Extremely slow -- Want to stay away from this.
# O(2^n) - Still slow  -- Want to stay away from this.
# O(n^2) - Still slow - Almost always associated with nested loops, (Brute force comparison and usually to slow).
# O(n log n) - Starting to speed up, still not ideal - Almost always related to sorting
# O(n) - Linear, not ideal but useful in some cases - Ex. Loops, traversing through list.
# O (log n) - Fast - Ex. Diving problems in half each time, binary search.
# O(1) - Instantaneous - Ex. Accessing index in an array, checking if x exists in a set.


## Hint - If the input is lower than 10^4 you can get away with O(n^2).
## If the input is lower than 10^5 you can get away with O (n loh n).
## Anything above 10^5, you NEED to optimize to get that time complexity down.

