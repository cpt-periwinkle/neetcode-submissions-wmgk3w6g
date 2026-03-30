class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        longest = 0
        for num in nums:
            if (num - 1) not in num_set:    # The first number in the series will not have a predecessor
                length = 0
                while (num + length) in num_set: # We want to check how many consecutive, so we for loop it
                    length += 1
                longest = max(longest, length) # takes the max between original and the current consecutive length

        return longest