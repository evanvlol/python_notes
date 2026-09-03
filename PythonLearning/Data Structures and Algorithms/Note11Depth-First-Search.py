# DFS is one of the most common way to explore tree or graph structures. DFS is about going deep, it doesnt care about
# layers. Only when DFS reaches the end of the path does it back up and explore other options.

# Key idea - explore one branch fully and then move to the next.

# 1. Explore every possibility.
# 2. Want to visit all nodes.
# 3. Care about structure, not distance.

# Because trees are acyclic, they are a perfect fit for DFS.
# Tree ex.

def someFunction(self, root):
    def dfs(node):
        if not node:
            return

        # process current node

        dfs(node.left)
        dfs(node.right)

    dfs(root)

# Good for flattening trees, building and checking structures, and searching for nodes based on custom logic.
# Graph ex.

def dfs(graph, start):
    visited = set()

    def search(node):
        if node in visited:
            return

        visited.add(node)

        # process current node here
        # print(node)

        for neighbor in graph[node]:
            search(neighbor)

    search(start)


