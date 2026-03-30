class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()     # stores indices of elements in decreasing order of values
        left = 0

        for right in range(len(nums)):
            # Maintain a monotonic decreasing deque:
            # Remove all indices from the back whose values are smaller than nums[right],
            # because they can never be the maximum for this or any future window
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            # Add current index to the deque
            q.append(right)

            # Remove the front index if it is outside the current window
            # (i.e., it is no longer within [left, right])
            if q[0] < left:
                q.popleft()

            # Once the window reaches size k, record the maximum (front of deque)
            if (right + 1) >= k:
                output.append(nums[q[0]])  # front of deque is the max
                left += 1                 # slide the window forward

        return output