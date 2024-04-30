/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
  const result = [];
  nums.sort((a, b) => a - b); // Sort the array
  const n = nums.length;

  for (let i = 0; i < n - 2; i++) {
      if (i === 0 || (i > 0 && nums[i] !== nums[i - 1])) { // Skip duplicate elements
          let left = i + 1;
          let right = n - 1;
          const target = -nums[i];

          while (left < right) {
              const sum = nums[left] + nums[right];

              if (sum === target) {
                  result.push([nums[i], nums[left], nums[right]]);
                  while (left < right && nums[left] === nums[left + 1]) left++; // Skip duplicate elements
                  while (left < right && nums[right] === nums[right - 1]) right--; // Skip duplicate elements
                  left++;
                  right--;
              } else if (sum < target) {
                  left++;
              } else {
                  right--;
              }
          }
      }
  }

  return result;
  
};

//Test cases
console.log(threeSum([-1, 0, 1, 2, -1, -4])); // Output: [[-1, -1, 2], [-1, 0, 1]]
console.log(threeSum([0, 1, 1])); // Output: []
console.log(threeSum([0, 0, 0])); // Output: [[0, 0, 0]]
