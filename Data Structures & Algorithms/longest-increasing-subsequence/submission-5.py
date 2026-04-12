class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # Edge case: no elements → no subsequence
        if not nums:
            return 0

        # table[i] = length of the longest increasing subsequence ENDING at index i
        # Every element alone is a subsequence of length 1
        table = [1] * len(nums)

        # Build the answer from left to right
        for i in range(len(nums)):

            # Look at all previous elements
            for j in range(i):

                # If current number can extend the subsequence ending at j
                if nums[i] > nums[j]:

                    # Either keep current best OR extend subsequence at j
                    table[i] = max(table[i], table[j] + 1)
        
        # The LIS could end anywhere, so take the maximum
        return max(table)