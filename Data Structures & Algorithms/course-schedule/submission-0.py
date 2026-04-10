from collections import defaultdict, deque
from typing import List

class Solution: # Kahn's Algorithm for Toposort
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # indegree[i] = number of prerequisites for course i
        indegree = [0] * numCourses

        # adjacency list: which courses depend on a given course
        adj = defaultdict(list)

        # Build graph
        for src, dst in prerequisites:
            # dst depends on src
            indegree[dst] += 1
            adj[src].append(dst)

        # Queue for courses we can take immediately (no prerequisites)
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        # Number of courses we are able to complete
        finish = 0

        # Process courses
        while q:
            node = q.popleft()
            finish += 1   # we "take" this course

            # This course unlocks its neighbors
            for nei in adj[node]:
                indegree[nei] -= 1   # one prerequisite satisfied

                # If no more prerequisites → ready to take
                if indegree[nei] == 0:
                    q.append(nei)

        # If we completed all courses → no cycle
        return finish == numCourses