/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
  nums.sort((a, b) => a - b); // Sort the array
  const n = nums.length;
  let closestSum = Infinity;

  for (let i = 0; i < n - 2; i++) {
      let left = i + 1;
      let right = n - 1;

      while (left < right) {
          const sum = nums[i] + nums[left] + nums[right];
          
          if (Math.abs(sum - target) < Math.abs(closestSum - target)) {
              closestSum = sum;
          }

          if (sum < target) {
              left++;
          } else if (sum > target) {
              right--;
          } else {
              // If sum equals target, return target
              return target;
          }
      }
  }

  return closestSum;
 
};

// Test cases
console.log(threeSumClosest([-1, 2, 1, -4], 1)); // Output: 2
console.log(threeSumClosest([0, 0, 0], 1)); // Output: 0
