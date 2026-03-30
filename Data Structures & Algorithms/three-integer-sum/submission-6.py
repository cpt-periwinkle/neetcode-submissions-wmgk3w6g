class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for curr in range(len(nums)):
            if (curr > 0 and nums[curr] == nums[curr - 1]):
                continue
            front = curr + 1
            back = len(nums) - 1
            while front < back:
                sum_val = nums[curr] + nums[front] + nums[back]
                if (sum_val == 0):
                    res.append([nums[curr], nums[front], nums[back]])
                    front += 1
                    back -= 1
                    while front < back and nums[front] == nums[front - 1]:
                        front += 1
                    while front < back and nums[back] == nums[back + 1]:
                        back -= 1
                elif (sum_val < 0):
                    front += 1
                else:
                    back -= 1
        
        return res