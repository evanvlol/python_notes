# Explore the structure level by level starting at the root or the source node.
# Then examine levels holistically until you reach the end.
# Useful because you can use the shortest number of steps to reach something, clean level-order traversal, and a way
# to explore everything.

# BFS Is utilized by a Queue, because we want to work with stuff and whatever comes in first will go out first.
# Trees are a special kind of graph with cycles, meaning we cannot loop back to a node that we have already visited.
# This makes BFS on trees more simple, because it ensures that we wont have any repeats.

# Template for BFS on trees.

from collections import deque

def bfs(root):
    queue = deque([root]) ## While the queue is not empty we remove the first node.
    while len(queue) > 0:
        node = queue.popleft()
        for child in node.children: ## If the child is not the goal, we add it to the queue and keep going. if it is return it.
            if is_goal(child):
                return FOUND(child)
            queue.append(child)
    return NOT_FOUND

# We need to use BFS when Traversing a tree from top to bottom
# Care about depth, distance, or levels.
# Looking for the first match/closest node to root.

# Graphs are more general than trees, they can have cycles, loops, and multiple connections between nodes, meaning
# you can revisit the same node if your not careful. This also means that we must keep track of visited nodes.
# Because otherwise we'll get stuck in an infinite loop or do redundant work.
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = {start}

    while queue:
        node = queue.popleft()

        # process node here
        print(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)




