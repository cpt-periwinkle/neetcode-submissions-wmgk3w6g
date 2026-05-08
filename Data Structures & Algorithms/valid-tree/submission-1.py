class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return False

        adj = defaultdict(list)
        for first, second in edges:
            adj[first].append(second)
            adj[second].append(first)

        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False

            visit.add(i)
            
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            
            return True
        
        return dfs(0, -1) and n == len(visit)