class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# Create instance for class MinStack
sol = MinStack()

# Test operations
operations = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
arguments = [[], [1], [2], [0], [], [], [], []]

results = []
for op, arg in zip(operations, arguments):
    if op == "push":
        sol.push(arg[0])
        results.append(None)
    elif op == "pop":
        sol.pop()
        results.append(None)
    elif op == "top":
        results.append(sol.top())
    elif op == "getMin":
        results.append(sol.getMin())

print(results)  # Expected output: [None, None, None, None, 0, None, 2, 1]
