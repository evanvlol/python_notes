# ============================================================
# DATA STRUCTURES NOTES
# ============================================================


# ============================================================
# 1. ARRAY / LIST
# ============================================================

# Stores multiple values in order.
# Elements can be accessed directly using an index.

nums = [10, 20, 30, 40]

# Access
nums[0]        # 10
nums[2]        # 30

# Add
nums.append(50)

# Remove
nums.pop()

# Concept:
# index:   0    1    2    3
#        [10] [20] [30] [40]



# ============================================================
# 2. LINKED LIST
# ============================================================

# A linked list is a chain of nodes.
# Each node stores:
#   1. A value
#   2. A pointer/reference to the next node
#
# A -> B -> C -> None


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Example
a = ListNode("A")
b = ListNode("B")
c = ListNode("C")

a.next = b
b.next = c

# Traversal
current = a

while current:
    # process current.val
    current = current.next



# ============================================================
# 3. STACK
# ============================================================

# Stack = Last In, First Out (LIFO)
#
# Think:
#
#   C  <- top
#   B
#   A
#
# C was added last, so C is removed first.


stack = []

# Push
stack.append("A")
stack.append("B")

# Look at top
top = stack[-1]

# Pop
value = stack.pop()

# General pattern
while stack:
    value = stack.pop()

    # process value



# ============================================================
# 4. QUEUE
# ============================================================

# Queue = First In, First Out (FIFO)
#
# Front              Back
#   A -> B -> C -> D
#
# A entered first, so A leaves first.


from collections import deque

queue = deque()

# Add to back
queue.append("A")
queue.append("B")

# Remove from front
value = queue.popleft()

# General pattern
while queue:
    value = queue.popleft()

    # process value



# ============================================================
# 5. TREE
# ============================================================

# A tree stores data in a hierarchy.
#
#         A
#        / \
#       B   C
#      / \
#     D   E
#
# Important terms:
#
# Root   = top node
# Parent = node above another node
# Child  = node below another node
# Leaf   = node with no children
#
# Binary Tree:
# Each node can have at most 2 children.


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Example
root = TreeNode("A")

root.left = TreeNode("B")
root.right = TreeNode("C")



# ============================================================
# 6. GRAPH
# ============================================================

# A graph stores nodes and the connections between them.
#
# Nodes = vertices
# Connections = edges
#
# Example:
#
# A ----- B
# |       |
# |       |
# C ----- D
#
# Graphs can contain cycles.
#
# A -> B -> C
# ^         |
# |_________|


# Common representation: adjacency list

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

# Access neighbors
neighbors = graph["A"]

# neighbors = ["B", "C"]



# ============================================================
# 7. SET
# ============================================================

# A set stores UNIQUE values.
# Duplicate values are not kept.
#
# Sets are useful when you need to quickly check:
# "Have I already seen this?"


visited = set()

# Add
visited.add("A")
visited.add("B")

# Check membership
if "A" in visited:
    pass

# Remove
visited.remove("A")



# ============================================================
# 8. DICTIONARY / HASH MAP
# ============================================================

# A dictionary stores:
#
# key -> value
#
# Example:
#
# name  -> John
# age   -> 18
# major -> CS


student = {
    "name": "John",
    "age": 18,
    "major": "CS"
}

# Access
student["name"]

# Add / Update
student["age"] = 19

# Check for key
if "name" in student:
    pass

# Remove
del student["major"]



# ============================================================
# QUICK SUMMARY
# ============================================================

# LIST
# Ordered collection with indexes
#
# nums = [1, 2, 3]


# LINKED LIST
# Nodes connected using .next
#
# A -> B -> C -> None


# STACK
# Last In, First Out
#
# append()
# pop()


# QUEUE
# First In, First Out
#
# append()
# popleft()


# TREE
# Hierarchical nodes
#
#       root
#      /    \
#   left    right


# GRAPH
# Nodes connected to other nodes
#
# graph[node] -> neighbors


# SET
# Unique values
#
# visited = set()


# DICTIONARY / HASH MAP
# key -> value
#
# dictionary[key] = value



# ============================================================
# IMPORTANT DISTINCTION
# ============================================================

# DATA STRUCTURES:
#
# Arrays / Lists
# Linked Lists
# Stacks
# Queues
# Trees
# Graphs
# Sets
# Dictionaries / Hash Maps


# ALGORITHMS / TECHNIQUES:
#
# Binary Search
# BFS
# DFS
# Backtracking
# Greedy
# Dynamic Programming