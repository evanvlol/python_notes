## Sets are one of the simplest data strucutres and most useful for time efficiency.
## A set is just a grouping of unique values with no duplicates and no particular order. ex. {a,b,c,d} not {a,a,a,a}
## Each value only appears once. If you wanted to see if a number was in a list, you could store it as a set and check for
## existence in constant time.

nums = [1,2,3,4,5]
seen = set(nums)
print(3 in seen)

## O(1) time complexity if done this way.

## When to use a set instead of a list.
## 1. When you care about uniqueness.
## 2. Existence, if you want to know if it was seen before.
## 3. Fast membership checks
## 4. Sliding window, and want to see if the elements are unique


