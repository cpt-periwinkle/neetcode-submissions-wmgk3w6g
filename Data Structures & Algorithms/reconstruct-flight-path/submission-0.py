class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Adjacency list:
        # adj[src] = list of destinations reachable from src
        adj = defaultdict(list)

        # Build the directed graph from the tickets
        for src, dest in tickets:
            adj[src].append(dest)
        
        # Sort destinations in reverse lexicographic order.
        #
        # Why reverse?
        # Because popping from the END of a Python list is O(1),
        # so after reverse sorting, pop() gives us the smallest
        # lexicographic destination efficiently.
        for lst in adj:
            adj[lst].sort(reverse=True)
        
        # This will store the itinerary in REVERSE order.
        res = []

        def dfs(airport):
            # Keep using tickets from this airport until none remain.
            #
            # Each pop() consumes a ticket permanently,
            # ensuring every ticket is used exactly once.
            while adj[airport]:

                # Get the lexicographically smallest available destination
                next_airport = adj[airport].pop()

                # Continue building the path from that airport
                dfs(next_airport)
            
            # IMPORTANT:
            # We only add the airport AFTER all outgoing tickets
            # from it have been used.
            #
            # This means dead ends get added first,
            # so the route is built backwards.
            res.append(airport)
        
        # The itinerary always starts from JFK
        dfs("JFK")

        # Since we built the route backwards,
        # reverse it to get the final itinerary.
        return res[::-1]