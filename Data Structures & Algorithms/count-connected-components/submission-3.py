class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        size = [1] * n
        
        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return 0
            
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a
            
            parent[root_b] = root_a
            size[root_a] += 1
            
            return 1
        
        components = n
        
        for a, b in edges:
            components -= union(a, b)
        
        return components