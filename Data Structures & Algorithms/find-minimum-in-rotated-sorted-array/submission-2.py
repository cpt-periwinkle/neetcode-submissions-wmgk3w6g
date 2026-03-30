class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize pointers for binary search
        left = 0
        right = len(nums) - 1

        # Store the minimum value found so far
        # Initialize with first element (safe starting point)
        res = nums[0]

        while left <= right:

            # ---- Optimization: Check if current subarray is already sorted ----
            # If nums[left] < nums[right], the entire range [left, right] is sorted
            # In a sorted array, the smallest element is always at 'left'
            # So we can update result and stop searching
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break  # no need to continue, we found the minimum in this segment

            # Compute mid safely (avoids overflow in other languages)
            mid = left + (right - left) // 2

            # Update result with mid element
            # Because mid could be the smallest element
            res = min(res, nums[mid])

            # ---- Decide which half to search ----
            # One half of the array is always sorted

            # Case 1: Left half is sorted
            # nums[left] <= nums[mid] means [left ... mid] is sorted
            if nums[mid] >= nums[left]:
                # Since left half is sorted, the minimum cannot be here
                # (we already considered nums[left] and nums[mid])
                # So move to the right half
                left = mid + 1

            else:
                # Case 2: Right half is sorted, so pivot (minimum) lies in left half
                right = mid - 1

        return res