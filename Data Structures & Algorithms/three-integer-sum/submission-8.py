class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []  # Stores all unique triplets that sum to 0
        
        nums.sort()  # Sort the array to enable two-pointer approach + duplicate handling

        for curr in range(len(nums)):
            # Skip duplicate values for the first element to avoid duplicate triplets
            if curr > 0 and nums[curr] == nums[curr - 1]:
                continue
            
            # Initialize two pointers for the remaining subarray
            front = curr + 1
            back = len(nums) - 1

            # Use two-pointer technique to find pairs that sum with nums[curr] to 0
            while front < back:
                target = nums[curr] + nums[front] + nums[back]

                # Found a valid triplet
                if target == 0:
                    res.append([nums[curr], nums[front], nums[back]])

                    # Move both pointers inward
                    front += 1
                    back -= 1

                    # Skip duplicates for 'front' pointer
                    # Compare with previous value since front was just incremented
                    while front < back and nums[front] == nums[front - 1]:
                        front += 1

                    # Skip duplicates for 'back' pointer
                    # Compare with next value since back was just decremented
                    while front < back and nums[back] == nums[back + 1]:
                        back -= 1

                # If sum is too large, decrease it by moving 'back' left
                elif target > 0:
                    back -= 1

                # If sum is too small, increase it by moving 'front' right
                else:
                    front += 1

        return res