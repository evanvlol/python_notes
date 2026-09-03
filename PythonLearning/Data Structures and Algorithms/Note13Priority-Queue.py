# A priority queue, also known as a Heap is a special type of queue where elements are removed in order of priority, and not
# just in the priority that they were added.

# Priority queues are usually implemented as binary heaps which are just binary trees stored in arrays.
# Two types, for Min Heaps the head is smaller than all of its children.
# For the Max heap the head is larger than all of its children.
# In python, the min heap is the default but you can do a max heap by (-) the values.
# Time complexity for insertion and removal are both O(log n).

# Show up in interview problems when
# You need to repeatedly extract the smallest/largest item
# Maintaining a top-k or bottom-k set of values.
# Real-time ranking, greedy selection, etc.
# Need to sort on the fly but not really tryna sort the entire array