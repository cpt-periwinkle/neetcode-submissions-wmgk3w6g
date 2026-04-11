from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Initially, every node is its own parent (n separate components)
        parent = list(range(n))

        # Size helps us keep trees balanced (union by size)
        size = [1] * n

        def find(x: int) -> int:
            # Find the root (representative) of x
            # Path compression flattens the tree for faster future lookups
            while x != parent[x]:
                parent[x] = parent[parent[x]]  # jump up and compress path
                x = parent[x]
            return x

        def union(a: int, b: int) -> int:
            # Find roots of both nodes
            root_a = find(a)
            root_b = find(b)

            # If already in same group, no merge happens
            if root_a == root_b:
                return 0

            # Attach smaller tree under larger tree (keeps tree shallow)
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b] = root_a
            size[root_a] += size[root_b]

            # Successfully merged → one less component
            return 1

        # Start with n components
        components = n

        # Each successful union reduces components by 1
        for a, b in edges:
            components -= union(a, b)

        return components