class MinStack:

    def __init__(self):
        self.stack = []
        self.min_values = [2 ** 31 - 1]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (val <= self.min_values[-1]):
            self.min_values.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if (popped == self.getMin()):
            self.min_values.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_values[-1]
        
