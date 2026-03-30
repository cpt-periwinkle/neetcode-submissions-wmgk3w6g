class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        min_k = right

        while left <= right:
            k = left + (right - left) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            
            if hours <= h:
                min_k = min(min_k, k)
                right = k - 1
            else:
                left = k + 1

        return min_k

