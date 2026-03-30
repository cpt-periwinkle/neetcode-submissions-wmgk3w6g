class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers:
        # 'front' starts at the beginning, 'back' at the end
        front = 0
        back = len(numbers) - 1

        # Continue until the pointers meet
        while front < back:
            # Compute the current sum of the two elements
            sum_val = numbers[front] + numbers[back]

            # If the sum matches the target, return 1-based indices
            if sum_val == target:
                return [front + 1, back + 1]

            # If sum is too large, decrease it by moving 'back' left
            elif sum_val > target:
                back -= 1

            # If sum is too small, increase it by moving 'front' right
            else:
                front += 1