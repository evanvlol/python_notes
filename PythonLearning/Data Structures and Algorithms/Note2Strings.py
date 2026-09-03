## Strings are just going to arrays of characters, and in most languages are immutable, which means they cannot be changed.
## If you modify a string, your not really changing the original, but rather creating a new string under the hood.
## For example..
chars =[]
result = ""
for char in chars:
    result += char

## This looks clean but is really creating a new string under every iteration, resulting in an O(n^2) time complexity.
## Instead you should be building an array of characters and joining them at the end to get back to O(n).
 result = []
 for char in chars:
     result.append(char)
     return "".join(result)

## Interview patterns in strings.
## 1. Find the longest substring without repeating characters.
## 2. Check if two strings are anagrams.
## 3. Return all substrings that match a pattern.


