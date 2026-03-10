# ============================================================
# Python Trees & Graphs - Foundations
# ============================================================

from collections import deque

# ---- TREE NODE ----

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ---- TREE TRAVERSALS ----

def inorder(root):          # left -> root -> right (gives sorted order in BST)
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def preorder(root):         # root -> left -> right
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def postorder(root):        # left -> right -> root
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]

def level_order(root):      # BFS - level by level
    if not root:
        return []
    result, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        result.append(level)
    return result

def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


# ---- GRAPH REPRESENTATIONS ----

# Adjacency list (most common for LeetCode)
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1],
}

# Build from edge list
edges = [[0,1], [1,2], [2,0]]
from collections import defaultdict
adj = defaultdict(list)
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)  # undirected


# ---- BFS ----

def bfs(graph, start):
    visited = {start}
    q = deque([start])
    while q:
        node = q.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)


# ---- DFS ----

def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def dfs_iterative(graph, start):
    visited = {start}
    stack = [start]
    while stack:
        node = stack.pop()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)


# ---- UNION-FIND (Disjoint Set Union) ----

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True
