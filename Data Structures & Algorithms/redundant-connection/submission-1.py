from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Nodes are labeled from 1 to n, and here n == len(edges)
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)  # size of each component tree

        def find(x):
            # Find the root of x
            # Path compression makes future finds faster
            while x != parent[x]:
                parent[x] = parent[parent[x]]  # move x closer to root
                x = parent[x]
            return x

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            # If both nodes already have the same root,
            # adding this edge creates a cycle
            if root_a == root_b:
                return False

            # Attach smaller tree under bigger tree
            if rank[root_a] < rank[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b] = root_a
            rank[root_a] += rank[root_b]

            return True

        for n1, n2 in edges:
            # The first edge that fails union is the redundant one
            if not union(n1, n2):
                return [n1, n2]

        return []