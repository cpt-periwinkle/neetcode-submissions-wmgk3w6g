class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = defaultdict(list)

        q = deque()

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        for course in range(len(indegree)):
            if indegree[course] == 0:
                q.append(course)
        
        res = []
        while q:
            course = q.popleft()
            res.append(course)
            for child in adj[course]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
            
        return [] if len(res) != numCourses else res