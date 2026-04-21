class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_arr, right_arr):
            l = r = 0
            res = []

            while l < len(left_arr) and r < len(right_arr):
                if left_arr[l] <= right_arr[r]:
                    res.append(left_arr[l])
                    l += 1
                else:
                    res.append(right_arr[r])
                    r += 1

            while l < len(left_arr):
                res.append(left_arr[l])
                l += 1
            
            while r < len(right_arr):
                res.append(right_arr[r])
                r += 1

            return res


        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left_sorted = self.sortArray(nums[:mid])
        right_sorted = self.sortArray(nums[mid:])
        return merge(left_sorted, right_sorted)
