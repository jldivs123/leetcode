# Problem 1 Two Sum

## Description

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Solution

1. Iterate over the array, get the difference between the target and current number.
2. If the difference exist in the hash return the current index and value from the hashmap
3. Otherwise, store the difference in the hashmap as "key" and save its index as value

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if num in d:
                return [i, d[num]]
            else:
                d[diff] = i
        # print(d)
        return []
```