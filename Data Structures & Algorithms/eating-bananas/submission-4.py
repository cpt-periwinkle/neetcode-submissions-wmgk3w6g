class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # We are binary searching on "k" (Koko's eating speed)
        # Minimum possible speed = 1 banana/hour
        left = 1

        # Maximum possible speed = max pile (eat largest pile in 1 hour)
        right = max(piles)

        # Stores the minimum valid speed found so far
        min_k = right

        # Binary search over possible speeds
        while left <= right:

            # Mid represents a candidate eating speed
            k = left + (right - left) // 2

            # Calculate total hours needed if Koko eats at speed k
            hours = 0
            for pile in piles:
                # For each pile:
                # time = ceil(pile / k) because partial hours count as full
                hours += math.ceil(pile / k)
            
            # If Koko can finish within h hours, k is a valid speed
            if hours <= h:
                # Try to minimize k (we want the smallest valid speed)
                min_k = min(min_k, k)

                # Search left half for a possibly smaller valid k
                right = k - 1

            else:
                # If it takes too long, k is too slow → increase speed
                left = k + 1

        return min_k