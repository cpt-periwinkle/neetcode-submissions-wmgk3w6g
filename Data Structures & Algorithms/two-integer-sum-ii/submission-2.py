class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front = 0
        back = len(numbers) - 1
        while (front < back):
            sum_val = numbers[front] + numbers[back]
            if (sum_val == target):
                return [front + 1, back + 1]
            elif (sum_val > target):
                back -= 1
            else:
                front += 1