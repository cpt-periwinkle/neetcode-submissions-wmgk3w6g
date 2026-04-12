class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # This is a variation of Kadane's Algorithm:
        # Instead of sum, we are tracking product.
        # The twist is that negatives flip signs, so we track BOTH max and min.

        # Initialize result as the maximum element
        # (handles cases where all numbers are negative)
        res = max(nums)

        # currMax = maximum product subarray ending at current index
        # currMin = minimum product subarray ending at current index
        # (needed because a negative number can flip min -> max)
        currMax, currMin = 1, 1

        for num in nums:
            # Store previous currMax * num before updating currMax
            # (because currMax will change and we still need the old value)
            temp = num * currMax

            # At each step, we have 3 choices:
            # 1. Extend previous max product subarray
            # 2. Extend previous min product subarray (important for negatives)
            # 3. Start a new subarray at current number
            currMax = max(temp, currMin * num, num)

            # Similarly track the minimum product (for future flips)
            currMin = min(temp, currMin * num, num)

            # Update global maximum product found so far
            res = max(res, currMax)

        return res