class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Think of this problem as:
        # "How do I build permutations step by step?"
        #
        # Idea:
        # - First get all permutations of a smaller problem
        # - Then insert the current element into every possible position

        # Base case:
        # If there are no numbers left, return one empty permutation
        # This acts as the "starting point" for building up results
        if len(nums) == 0:
            return [[]]

        # Get permutations of the smaller list (everything except nums[0])
        perms = self.permute(nums[1:])

        res = []

        # Now take the current number (nums[0])
        # and "weave" it into every possible position
        for p in perms:
            # If p has length k, there are k+1 places to insert:
            # before, between elements, and after
            for i in range(len(p) + 1):
                # Copy because we don't want to modify the original permutation
                p_copy = p.copy()

                # Insert current number into position i
                # This creates a new unique permutation
                p_copy.insert(i, nums[0])

                # Add the newly formed permutation
                res.append(p_copy)

        # By doing this for all smaller permutations,
        # we generate all permutations of nums
        return res