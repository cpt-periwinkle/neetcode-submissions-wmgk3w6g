class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]     # to not lose track of the positions
        pair.sort(reverse = True)
        stack = []
        for p, s in pair:
            stack.append((target - p) / s)
            if (len(stack) >= 2 and stack[-1] <= stack[-2]):    # we check only if the stack has 2 or more elements (otherwise only one fleet exists) and we then compare what we just put with the previous for finding whatever is lesser
                stack.pop() # crux of the problem is that the car in the later positions will always slow down cars at positions behind it, so we can ignore them once/ if they reach each other
        return len(stack)

        