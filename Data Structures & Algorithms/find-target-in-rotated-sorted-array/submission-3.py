class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize pointers for binary search
        left = 0
        right = len(nums) - 1

        # Continue while there is a valid search space
        while left <= right:
            # Compute mid index
            mid = left + (right - left) // 2

            # If we find the target, return its index
            if target == nums[mid]:
                return mid

            # ---- Determine which half is sorted ----

            # Case 1: Left half is sorted
            # If nums[left] <= nums[mid], then [left ... mid] is sorted
            if nums[left] <= nums[mid]:

                # Check if target lies OUTSIDE this sorted left half
                # If target > nums[mid] OR target < nums[left],
                # then it cannot be in this left half
                if target > nums[mid] or target < nums[left]:
                    # Discard left half, search right half
                    left = mid + 1
                else:
                    # Target lies within sorted left half
                    right = mid - 1

            # Case 2: Right half is sorted
            else:
                # If left half is not sorted, right half must be sorted

                # Check if target lies OUTSIDE this sorted right half
                # If target < nums[mid] OR target > nums[right],
                # then it cannot be in this right half
                if target < nums[mid] or target > nums[right]:
                    # Discard right half, search left half
                    right = mid - 1
                else:
                    # Target lies within sorted right half
                    left = mid + 1

        # Target not found
        return -1