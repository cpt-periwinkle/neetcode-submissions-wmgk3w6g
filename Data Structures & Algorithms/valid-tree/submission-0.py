from collections import defaultdict
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Edge case: empty graph is considered a tree
        if not n:
            return True

        # Build adjacency list for undirected graph
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(i, prev):
            # If we've already seen this node, we found a cycle
            if i in visit:
                return False

            visit.add(i)

            # Explore all neighbors
            for j in adj[i]:
                # Skip the node we came from (avoid false cycle)
                if j == prev:
                    continue

                # If any path detects a cycle, propagate False
                if not dfs(j, i):
                    return False

            return True

        # Two conditions:
        # 1. DFS should not detect a cycle
        # 2. All nodes must be visited (graph is connected)
        return dfs(0, -1) and n == len(visit)