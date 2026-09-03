# Binary search is one of the most efficient algorithms in computer science. Its meant to take a big problem and cut it in half
# over and over again until you get to the correct answer.

# instead of scanning from start to finish O(N), binary search allows you to find the answer in O(log n) time.
# Binary search is much more powerful than just searching for a number though.

# Vanilla binary search template.
# Binary Search
# Requirement: nums must be sorted

left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

return -1

# Always use Binary search when your directly for a number within an array.
# In the vanilla array we needed a sorted array to do so. But we actually dont need a sorted array at all.
# All we need is a Monotonic condition, just to say that the condition only changes in one direction.
# Having a sorted array is a monotonic condition but its not the only one.