## Sliding windows are like two pointers, but instead of managing just two positions, your managing a range of positions.
from os import remove


## For example, check 1-3, then slide 2-4.

## For clarity your only caring about what is in the window, to see a subset of the data, not revisiting the same element twice.
## This reduces time complexity to O(n).

## Two types of sliding window patterns, fixed size (where the size stays the same throughout) and dynamic (where the window can
## shrink or expand as necessary).

# A fixed window size is used when the problem gives you a specific window size to use.
# ex. Find the minimum average of any subarray of size k."
# ex. Return the sum of every k-len block
# ex. Find the subarray of length k with the largest/smallest X.

## Template your likely to see.

def sliding_windows_fixed(input, window_size):
    ans = window = input[0:window_size] # This grabs the first window size elements as our initial windows.
    for right in range(window_size, len(input)): # Loop from window size to end of input.
        left = right - window_size # Each step we calculate left as right - window size to give us the index of what just fell out the window
        remove input[left] from window # Remove the old element.
        append input[right] to window # Add the new input
        ans = optimal(ans,window) # Then update the answer based on what the problem is asking.
    return ans

# Dynamic sized window

# Used when the window size is not fixed. And trying to find an optimal range that satisfies a condition.
# ex. Find the length of the longest substring with at most K unique characters.
# ex. Whats the smallest subarray with a sum greater than a target.
# ex. Return the longest window where a certain rule is valid.

# In these problems, this window can grow or shrink depending on the data.

# Your likely to see.
def sliding_window_flexible_longest(input):
    initialize window, ans # Start with an empty element and grow it once every time from the right.
    left = 0
    for right in range(len(input)): # Once you add a new window you check if the window is still valid.
        append input[right] to window
        while invalid(window):  # Once its valid you update your answer.
            remove input[left] from window
            left += 1   # If its invalid you start removing elements from the left until it becomes valid again.
        ans = max(ans, window)
        return ans


