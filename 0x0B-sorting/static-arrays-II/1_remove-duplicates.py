from typing import List

class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    l = 1

    for r in range(1, len(nums)):
      if nums[r] != nums[r - 1]:
        nums[l] = nums[r]
        l += 1
    return l

# create an instance for solution class 
sol = Solution()

nums = [0,0,1,1,1,2,2,3,3,4]
new_length = sol.removeDuplicates(nums)

print(new_length) # output: 5
print("", nums[:new_length]) # output [0,1,2,3,4]
