from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Each node starts in its own component.
        parent = list(range(n))
        size = [1] * n  # size[i] = number of nodes in the tree whose root is i

        def find(x: int) -> int:
            # Find the root of x with path compression.
            while x != parent[x]:
                parent[x] = parent[parent[x]]  # compress path
                x = parent[x]
            return x

        def union(a: int, b: int) -> int:
            # Union by size.
            root_a = find(a)
            root_b = find(b)

            # Already in the same component, so no merge happened.
            if root_a == root_b:
                return 0

            # Attach smaller tree under larger tree.
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b] = root_a
            size[root_a] += size[root_b]

            # One successful union means one fewer connected component.
            return 1

        components = n

        for a, b in edges:
            components -= union(a, b)

        return components