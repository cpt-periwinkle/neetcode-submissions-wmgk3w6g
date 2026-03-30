class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)    # will always be as long as the temperatures list, and default value is 0
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:  # checks if stack is not empty and if the current stack top is less than current temperature
                top = stack.pop()           # if it is less, than we pop the top as we have found the greatest value for that specific
                result[top] = i - top       # subtract so we get the actual value for that day
            stack.append(i)                 # if current temp is lesser we just append until we find a greater element

        return result

