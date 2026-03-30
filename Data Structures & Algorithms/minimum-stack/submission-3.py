class MinStack:

    def __init__(self):
        self._stack = []
        self._min_stack = []        # two stacks to track minimum. Min stack only keeps minimum values and scraps any non minimums

    def push(self, val: int) -> None:
        self._stack.append(val)

        if not self._min_stack or val <= self._min_stack[-1]:   # check if min stack is empty or if the current value is lesser than current minimum
            self._min_stack.append(val)     # adds that element

    def pop(self) -> None:
        if self._stack[-1] == self._min_stack[-1]:      # checks for element being popped is a minimum so if true, next minimum element can take its place
            self._min_stack.pop()
        self._stack.pop()
        

    def top(self) -> int:
        return self._stack[-1]
        

    def getMin(self) -> int:
        return self._min_stack[-1]
