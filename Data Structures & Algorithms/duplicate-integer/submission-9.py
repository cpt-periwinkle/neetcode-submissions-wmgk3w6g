class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums == []:
            return False

        visited = set()
        for i in nums:
            if i in visited:
                return True
            visited.add(i)
        
        return False
        