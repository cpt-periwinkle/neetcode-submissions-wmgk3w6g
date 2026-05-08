class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = defaultdict(list)

        q = deque()

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            course = q.popleft()
            numCourses -= 1
            for child in adj[course]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
        
        return numCourses == 0