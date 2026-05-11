# Prim's Algorithm
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Number of points/nodes in the graph
        N = len(points)

        # Build adjacency list:
        # adj[i] = list of [distance, neighbor]
        #
        # Since every point can connect to every other point,
        # this is a complete graph.
        adj = {i: [] for i in range(N)}

        # Compute Manhattan distance between every pair of points
        for i in range(N):
            x1, y1 = points[i]

            for j in range(i + 1, N):
                x2, y2 = points[j]

                # Manhattan distance formula
                dist = abs(x1 - x2) + abs(y1 - y2)

                # Undirected graph:
                # i <-> j
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        # Final minimum cost of the MST
        res = 0

        # Stores points already included in the MST
        visit = set()

        # Min heap stores:
        # [cost to connect this point, point index]
        #
        # Start from point 0 with cost 0
        min_heap = [[0, 0]]

        # Continue until all points are connected
        while len(visit) < N:

            # Get the cheapest edge currently available
            next_cost, next_point = heapq.heappop(min_heap)

            # A point may appear multiple times in the heap
            # through different edges.
            #
            # If this point was already added to the MST,
            # skip this outdated entry.
            if next_point in visit:
                continue

            # Add this point to the MST
            visit.add(next_point)

            # Add the edge cost used to connect it
            res += next_cost

            # Explore all neighbors of this point
            for cost, point in adj[next_point]:

                # Only consider points not already in the MST
                if point not in visit:

                    # Add candidate edge to the heap
                    heapq.heappush(min_heap, [cost, point])
        
        # Total cost of the minimum spanning tree
        return res