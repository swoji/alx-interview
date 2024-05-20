class Solution:
    def isValid(self, s: str) -> bool:
      stack = []
      closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

      for c in s:
        if c in closeToOpen:
          if stack and stack[-1] == closeToOpen[c]:
            stack.pop()
          else:
            return False
        else:
          stack.append(c)

      return not stack

# create instance for class Solution
sol = Solution()
test_strings = ["[]", "([{}])", "[(])"]
results = [sol.isValid(s) for s in test_strings]
print(results) # output: [True, True, False]
