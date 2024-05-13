from typing import List

class Solution:
  def replaceElements(self, arr: List[int]) -> List[int]:
    # initial max = -1
    # reverse iteration
    # new max = max(oldmax, arr[i])

    rightMax = -1

    for i in range(len(arr) - 1, -1, -1):
      newMax = max(rightMax, arr[i])
      arr[i] = rightMax
      rightMax = newMax
    return arr
  
# Create an instance of the Solution class
sol = Solution()

# Call the replaceElements method through the instance
print (sol.replaceElements([17,18,5,4,6,1])) # output: [[18, 6, 6, 6, 1, -1]]
