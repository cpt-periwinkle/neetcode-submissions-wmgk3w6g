class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_length = len(nums)
        product_array = [1] * arr_length

        prefix = 1      # to set first variable to not 0
        for i in range(arr_length): # to get first half of the multiplications
            product_array[i] *= prefix  # first set prefix and then change prefix so current index not present
            prefix *= nums[i]   # updated the prefix for the next go around. On last element it's lost

        suffix = 1
        for j in range(arr_length - 1, -1, -1):         # reversed so as to get the back half
            product_array[j] *= suffix  # first set suffix and then change suffix so current index not present
            suffix *= nums[j]   # updated the suffix for the next go around. On first element it's lost

        return product_array