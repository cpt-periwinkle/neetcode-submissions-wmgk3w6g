class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for curr in range(len(nums)):
            if (curr > 0 and nums[curr] == nums[curr - 1]):     # To make sure to skip duplicates
                continue
            
            front = curr + 1
            back = len(nums) - 1
            while (front < back):
                target = nums[curr] + nums[front] + nums[back]

                if (target == 0):
                    res.append([nums[curr], nums[front], nums[back]])
                    front += 1
                    back -= 1
                    while (front < back and nums[front] == nums[front - 1]):    # To make sure to skip duplicates
                        front += 1
                    while (front < back and nums[back] == nums[back + 1]):      # To make sure to skip duplicates
                        back -= 1

                elif (target > 0):
                    back -= 1
                else:
                    front += 1
        return res
