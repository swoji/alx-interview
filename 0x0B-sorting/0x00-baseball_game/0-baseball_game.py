from typing import List

class Solution:
  def calPoints(self, ops: List[str]) -> int:
    stack = []

    for op in ops:
      if op == "+":
        stack.append(stack[-1] + stack[-2])
      elif op == "D":
        stack.append(2 * stack[-1])
      elif op == "C":
        stack.pop()
      else:
        stack.append(int(op))

    return sum(stack)

# create an instance for solution class  
sol = Solution()
ops = ["5","-2","4","C","D","9","+","+"]
new_stack = sol.calPoints(ops)
print(new_stack) # output: 27
