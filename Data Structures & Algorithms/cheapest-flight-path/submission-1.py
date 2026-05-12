class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # prices[i] =
        # cheapest cost currently known to reach city i
        prices = [float('inf')] * n

        # Cost to reach source city from itself is 0
        prices[src] = 0

        # Bellman-Ford algorithm:
        #
        # Relax all edges k + 1 times.
        #
        # Why k + 1?
        # Because:
        # k stops means we can use at most k + 1 flights/edges.
        for i in range(k + 1):

            # Important:
            # Use a copy so updates made during THIS iteration
            # do not affect other relaxations in the same round.
            #
            # This ensures each iteration only uses paths
            # with at most i + 1 edges.
            temp_prices = prices.copy()

            # Try relaxing every flight/edge
            for s, d, p in flights:

                # If source city is currently unreachable,
                # we cannot use this flight yet.
                if prices[s] == float('inf'):
                    continue

                # Relaxation step:
                #
                # Can we reach destination d more cheaply
                # by first reaching s, then taking this flight?
                if (prices[s] + p) < temp_prices[d]:

                    # Update cheaper price
                    temp_prices[d] = prices[s] + p
            
            # Move to next iteration
            prices = temp_prices
        
        # If destination is still infinity,
        # it was unreachable within k stops.
        return prices[dst] if prices[dst] != float('inf') else -1