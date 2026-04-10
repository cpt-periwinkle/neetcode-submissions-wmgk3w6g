from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # indegree[i] = number of prerequisites needed for course i
        indegree = [0] * numCourses

        # adjacency list: prereq -> list of courses unlocked after taking it
        adj = defaultdict(list)

        # Build the graph
        # [dst, src] means: src must be done before dst (src -> dst)
        for dst, src in prerequisites:
            indegree[dst] += 1           # dst has one more prerequisite
            adj[src].append(dst)         # src unlocks dst

        # Queue for courses that can be taken immediately (no prerequisites)
        q = deque()

        for i, num in enumerate(indegree):
            if num == 0:
                q.append(i)

        res = []

        # Process courses in BFS order
        while q:
            node = q.popleft()
            res.append(node)  # we can safely take this course now

            # This course unlocks its neighbors
            for num in adj[node]:
                indegree[num] -= 1       # remove one prerequisite
                if indegree[num] == 0:   # now ready to take
                    q.append(num)

        # If we processed all courses, return order
        # Otherwise, there is a cycle (impossible to finish)
        return res if len(res) == numCourses else []