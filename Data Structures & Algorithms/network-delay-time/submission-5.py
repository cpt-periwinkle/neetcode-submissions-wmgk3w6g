class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build an adjacency list:
        # edges[a] stores all nodes that can be reached from node a,
        # along with the time it takes to reach them.
        edges = defaultdict(list)

        for a, b, t in times:
            edges[a].append((b, t))

        # Min heap stores pairs of:
        # (time taken so far to reach this node, current node)
        #
        # We start at node k with time 0.
        min_heap = [(0, k)]

        # visited stores nodes whose shortest time has already been finalized.
        visited = set()

        # This will track the largest shortest-time among all reached nodes.
        # In other words, the time when the last reachable node receives the signal.
        total_time = 0

        while min_heap:
            # Always process the node with the smallest current travel time.
            # This is the key idea of Dijkstra's algorithm.
            t1, n1 = heapq.heappop(min_heap)

            # If we already finalized this node before, skip it.
            # The heap may contain older/worse paths to the same node.
            if n1 in visited:
                continue

            # The first time we pop a node from the min heap,
            # we know this is the shortest possible time to reach it.
            visited.add(n1)

            # Since nodes are finalized in increasing time order,
            # the latest finalized time becomes the current answer.
            total_time = t1

            # Try sending the signal from this node to all of its neighbors.
            for n2, t2 in edges[n1]:
                # Only consider neighbors whose shortest time is not finalized yet.
                if n2 not in visited:
                    # Time to reach neighbor = time to reach current node
                    # plus edge time from current node to neighbor.
                    heapq.heappush(min_heap, (t1 + t2, n2))

        # If we visited all n nodes, total_time is when the last node got the signal.
        # Otherwise, some node was unreachable, so return -1.
        return total_time if len(visited) == n else -1