from collections import defaultdict, deque
from typing import List

class Solution:  # Kahn's Algorithm for Toposort
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # indegree[i] = number of prerequisites required for course i
        indegree = [0] * numCourses

        # adjacency list: for each course, which courses depend on it
        # key = src (prerequisite), value = list of courses unlocked after taking src
        adj = defaultdict(list)

        # Build graph
        for dst, src in prerequisites:
            # dst depends on src, so we draw an edge: src -> dst
            # meaning: if we complete src, we can move toward dst
            adj[src].append(dst)

            # dst has one more prerequisite (src)
            indegree[dst] += 1

        # Queue for courses that have no prerequisites
        # these can be taken immediately
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        # Count how many courses we are able to complete
        finish = 0

        # Process courses in BFS order
        while q:
            node = q.popleft()

            # We are "taking" this course
            finish += 1

            # This course unlocks its dependent courses
            for nei in adj[node]:
                # One prerequisite for nei is now satisfied
                indegree[nei] -= 1

                # If nei has no more prerequisites, we can take it
                if indegree[nei] == 0:
                    q.append(nei)

        # If we processed all courses, there is no cycle
        # otherwise, a cycle exists and some courses could not be completed
        return finish == numCourses