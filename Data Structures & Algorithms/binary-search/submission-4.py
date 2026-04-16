class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def search(l, r):
            if l > r:
                return -1

            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return search(mid + 1, r)
            else:
                return search(l, mid - 1)

        return search(0, len(nums) - 1)